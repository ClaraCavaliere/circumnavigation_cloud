#!/usr/bin/python


import rospy as rp
import geomtwo.msg as gms
import geomtwo.impl as gmi
import std_msgs.msg as smsp
import threading as thd
import numpy as np
import math
import cloud1.srv as srvc
import cloud1.msg as cms


rp.init_node('cloud_agent_info')

AGENT_NAMES = rp.get_param('agent_names').split()
sensorMsrm_proxy = dict()
bearing_measurement = dict()
FREQUENCY = 60.0
RATE = rp.Rate(FREQUENCY)


LOCK=thd.Lock()


for name in AGENT_NAMES:
     rp.wait_for_service(name+'/Sensor_Service')
     sensorMsrm_proxy[name] = rp.ServiceProxy(name+'/Sensor_Service', srvc.SensorService)
    


def cloud_handler(req):
	LOCK.acquire()
	neigh_meas = bearing_measurement[req.neighID]
	LOCK.release()
	return srvc.CloudServiceResponse(neigh_meas)

rp.Service('Cloud_Service', srvc.CloudService, cloud_handler)



while not rp.is_shutdown(): 
	for name in AGENT_NAMES:
		 resp = sensorMsrm_proxy[name].call()
		 bearing_measurement[resp.ID] = gmi.Vector(resp.bear_msrm)
  
	RATE.sleep()














