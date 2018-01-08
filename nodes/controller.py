#! /usr/bin/python

import rospy as rp
import geomtwo.msg as gms
import geomtwo.impl as gmi
import std_msgs.msg as smsp
import threading as thd
import numpy as np
import math
from std_msgs.msg import Float32
import circumnavigation_cloud.srv as srvc
import geometry_msgs.msg as gm


rp.init_node('controller')

#Parameters and variables
position = None
alpha = rp.get_param('alpha')
distance = None
TARGET_POSITION = rp.get_param('target_position')
DESIRED_DISTANCE = rp.get_param('desired_distance')
agent_name = rp.get_param('agentID')
angle = 0.0



#Lock
LOCK = thd.Lock()


#Counterclockwise_angle function
def Counterclockwise_angle(bearing_measurement,neighbor_bearing_measurement):
    phi_i=np.array([bearing_measurement[0],bearing_measurement[1],0.0])
    phi_j=np.array([neighbor_bearing_measurement[0],neighbor_bearing_measurement[1],0.0])
    n_i=np.linalg.norm(phi_i)
    n_j=np.linalg.norm(phi_j)
    sp=np.inner(phi_i,phi_j)
    vp=np.cross(phi_i,phi_j)
    cos_beta=sp/(n_i*n_j)
    sin_beta=vp[2]/(n_i*n_j)
    beta_angle=math.atan2(sin_beta,cos_beta)
    if beta_angle<0:
        beta_angle=beta_angle+2*math.pi
    return beta_angle

#Subscribers
def position_callback(msg):
        global position
        LOCK.acquire()
        position = np.array([msg.x, msg.y])
        LOCK.release()
rp.Subscriber(
        name = 'position',
        data_class = gms.Vector,
        callback = position_callback,
        queue_size = 1)


#Call to the service 'Sensor_Service'
rp.wait_for_service('Sensor_Service')
sensor_proxy = rp.ServiceProxy('Sensor_Service', srvc.SensorService)
resp = sensor_proxy()
bearing_measurement = resp.bear_msrm
bear_ref = bearing_measurement


tacs = rp.get_time()
vel = 0.0
#Call to the service '/Cloud_Service'
rp.wait_for_service('/Cloud_Service')
cloud_proxy = rp.ServiceProxy('/Cloud_Service', srvc.CloudService)
cloud_resp = cloud_proxy(str(agent_name), bearing_measurement, vel, tacs) 
beta = cloud_resp.beta
angle = beta

RATE = rp.Rate(60.0)
start = False

#Publisher
cmdvel_pub = rp.Publisher(
      name = 'cmdvel',
      data_class = Float32,
      queue_size = 10)


#Publisher 'beta' (for bagfile)
beta_pub = rp.Publisher(
    name='beta',
    #data_class=gm.ff,
    data_class=Float32,
    queue_size=10)




           
# while not rp.is_shutdown():
#   tf = rp.get_time()
#   resp = sensor_proxy()
#   bearing_measurement = resp.bear_msrm
#   angle = Counterclockwise_angle(np.array([bear_ref.x,bear_ref.y]),([bearing_measurement.x,bearing_measurement.y]))
#   if (tf-ti)>0.1:
#     #cloud_resp = cloud_proxy(str(agent_name), bearing_measurement)
#     cloud_resp = cloud_proxy(str(agent_name), bearing_measurement, vel)
#     ti = rp.get_time()
#   estimate_neigh_pos = gmi.Vector(cloud_resp.bear_msrm_neigh).rotate(cloud_resp.control_signal_neigh)
#   beta = Counterclockwise_angle(np.array([bearing_measurement.x, bearing_measurement.y]), np.array([estimate_neigh_pos.x, estimate_neigh_pos.y]))
#   #beta = cloud_resp.beta


##Event triggered
# while not rp.is_shutdown():
#   ti = rp.get_time()
#   resp = sensor_proxy()
#   bearing_measurement = resp.bear_msrm
#   angle = Counterclockwise_angle(np.array([bear_ref.x,bear_ref.y]),([bearing_measurement.x,bearing_measurement.y]))
#   if angle>=beta:
#     cloud_resp = cloud_proxy(str(agent_name), bearing_measurement, vel)
#     bear_ref = bearing_measurement
#   beta = cloud_resp.beta

tprec = 0.0

while not rp.is_shutdown():
  tcorr = rp.get_time()
  resp = sensor_proxy()
  bearing_measurement = gmi.Vector(resp.bear_msrm)
  angle = Counterclockwise_angle(np.array([bear_ref.x,bear_ref.y]),([bearing_measurement.x,bearing_measurement.y]))
  if angle>=beta:
    req = srvc.CloudServiceRequest(str(agent_name), bearing_measurement, vel, tcorr)
    cloud_resp = cloud_proxy(req)
    bear_ref = gmi.Vector(bearing_measurement)
    estimate_neigh_pos = gmi.Vector(cloud_resp.bear_msrm_neigh).rotate(cloud_resp.control_signal_neigh*(tcorr-float(cloud_resp.t_neigh)))
    beta = Counterclockwise_angle(np.array([bearing_measurement.x, bearing_measurement.y]), np.array([estimate_neigh_pos.x, estimate_neigh_pos.y]))
  
  LOCK.acquire()

  distance = np.linalg.norm(TARGET_POSITION-position)

  #Control law
  vel = 0.2*distance*(alpha+beta)
 
  LOCK.release()

  #Publishing
  cmdvel_pub.publish(vel)
  beta_pub.publish(beta)

  RATE.sleep()
   


       








