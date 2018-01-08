#!/usr/bin/python


import rospy as rp
import geomtwo.msg as gms
import geomtwo.impl as gmi
import std_msgs.msg as smsp
import threading as thd
import numpy as np
import math
import circumnavigation_cloud.srv as srvc



rp.init_node('cloud_agent_info')

AGENT_NAMES = rp.get_param('agent_names').split()
sensorMsrm_proxy = dict()
bearing_measurement = dict()
control_values = dict()
instant_access = dict()
beta = dict()
FREQUENCY = 100.0
RATE = rp.Rate(FREQUENCY)

LOCK=thd.Lock()

#Counterclockwise_angle function
def Counterclockwise_angle(bearing_measurement,neighbor_bearing_measurement,agent):
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
    return beta_angle, agent


def cloud_handler(req):
    tcorr = rp.get_time()
    bearing_measurement[req.ID] = np.array([req.bear_msrm.x, req.bear_msrm.y])
    control_values[req.ID] = req.control_signal
    instant_access[req.ID] = req.time_access
    
    while len(bearing_measurement) < len(AGENT_NAMES):
        rp.sleep(0.1)
    
    betas = [Counterclockwise_angle(bearing_measurement[req.ID], meas, agent) for agent, meas in bearing_measurement.items() if agent != req.ID]
    beta_neigh = min(betas, key=lambda x: x[0])
    #return srvc.CloudServiceResponse(beta_neigh[0])
    resp = srvc.CloudServiceResponse()
    resp.beta = beta_neigh[0]
    bear_arr = np.array(bearing_measurement[beta_neigh[1]])
    resp.bear_msrm_neigh = gmi.Vector(bear_arr[0], bear_arr[1])
    resp.control_signal_neigh = control_values[beta_neigh[1]]
    resp.t_neigh = instant_access[beta_neigh[1]] 
    return resp
    

rp.Service('Cloud_Service', srvc.CloudService, cloud_handler)

rp.spin()














