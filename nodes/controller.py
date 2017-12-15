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
neigh_name = rp.get_param('neighID')



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
    beta=math.atan2(sin_beta,cos_beta)
    if beta<0:
        beta=beta+2*math.pi
    return beta



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

#Call to the service '/Cloud_Service'
rp.wait_for_service('/Cloud_Service')
cloud_proxy = rp.ServiceProxy('/Cloud_Service', srvc.CloudService)
cloud_resp = cloud_proxy(str(neigh_name)) 



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


ti = rp.get_time()
#five_sec_rate = rp.Rate(0.2)
while not rp.is_shutdown() and not start:
    tf = rp.get_time()
    if (tf-ti)>2:
      cloud_resp = cloud_proxy(str(neigh_name)) 
      ti = rp.get_time()
    resp = sensor_proxy()
    bearing_measurement = np.array([resp.bear_msrm.x, resp.bear_msrm.y])
    neigh_bear_meas = np.array([cloud_resp.neigh_bear_vector.x, cloud_resp.neigh_bear_vector.y])
    LOCK.acquire()

    if all([not data is None for data in [position, bearing_measurement, neigh_bear_meas]]):
      start = True      
    LOCK.release()
    RATE.sleep()

           
while not rp.is_shutdown():
  tf = rp.get_time()
  if (tf-ti)>2:
    cloud_resp = cloud_proxy(str(neigh_name)) 
    ti = rp.get_time()
  resp = sensor_proxy()
  bearing_measurement = np.array([resp.bear_msrm.x, resp.bear_msrm.y])
  neigh_bear_meas = np.array([cloud_resp.neigh_bear_vector.x, cloud_resp.neigh_bear_vector.y])
  LOCK.acquire()

  #Bearing vector in the clockwise direction
  phi_bar = np.array([bearing_measurement[1], -bearing_measurement[0]])

  #Counterclockwise angle
  beta = Counterclockwise_angle(bearing_measurement, neigh_bear_meas)
  distance = np.linalg.norm(TARGET_POSITION-position)

  #Control law
  vel = 0.3*distance*(alpha+beta)
 
  LOCK.release()

  #Publishing
  cmdvel_pub.publish(vel)
  beta_pub.publish(beta)

  RATE.sleep()
   


       








