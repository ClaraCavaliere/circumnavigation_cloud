#! /usr/bin/python

import rospy as rp
import geomtwo.msg as gms
import geomtwo.impl as gmi
import threading as thd
import numpy as np
import circumnavigation_cloud.srv as srvc

TARGET_POSITION = np.array(rp.get_param('target_position')) #from the .yaml file
bearing = None
position = None
agent_name = rp.get_param('agentID')

#Lock
LOCK = thd.Lock()

rp.init_node('sensor_simulator')


#Subscriber
def position_callback(msg):
    global position
    LOCK.acquire()
    position = np.array([msg.x, msg.y])
    LOCK.release()
rp.Subscriber(
    name='position',
    data_class = gms.Vector,
    callback=position_callback,
    queue_size=10)




rp.wait_for_message('position', gms.Vector)


#Handler for the service SensorService
def sensor_srvc_handler(req):
    LOCK.acquire()
    #Bearing vector (phi)
    bearing = (TARGET_POSITION-position)/np.linalg.norm(TARGET_POSITION-position)
    LOCK.release()
    return srvc.SensorServiceResponse(gmi.Vector(bearing[0], bearing[1]))

rp.Service('Sensor_Service', srvc.SensorService, sensor_srvc_handler)


rp.spin()


