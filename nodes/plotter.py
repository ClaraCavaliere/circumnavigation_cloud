#! /usr/bin/python 

import rospy as rp 
import geomtwo.msg as gms
import numpy as np
import threading as thd
import copy as cp 
import std_msgs.msg as smsp
import matplotlib.pyplot as plt
import math

rp.init_node('plotter')


RATE = rp.Rate(3.0e1)

AGENT_COLOR = rp.get_param('agent_color')
TARGET_COLOR = rp.get_param('target_color')

AGENT_NAMES = rp.get_param('agent_names').split()
TARGET_POSITION = rp.get_param('target_position')



LOCK = thd.Lock()

plt.ion()
plt.figure()
plt.scatter(*TARGET_POSITION, color=TARGET_COLOR)
circle=plt.Circle(TARGET_POSITION, 1.0, color='r', fill=False, linestyle='dashed')
ax = plt.gca()
ax.add_patch(circle)
plt.axis('equal')
plt.grid(True)
plt.draw()

agent_positions = {name: None for name in AGENT_NAMES}
agent_artists = {name: None for name in AGENT_NAMES}



#Subscriber
def agent_callback(msg,name):
    global agent_positions
    LOCK.acquire()
    agent_positions[name] =  [msg.x, msg.y]
    LOCK.release()
for name in AGENT_NAMES:
    rp.Subscriber(
    name = name+'/position',
    #data_class = gms.Point,
    data_class = gms.Vector,
    callback = agent_callback,
    callback_args = name,
    queue_size = 1)



while not rp.is_shutdown():
    ag_pos = {name: None for name in AGENT_NAMES}
    ag_posVet = {name: None for name in AGENT_NAMES}

    LOCK.acquire()
    for name in AGENT_NAMES:
            if not agent_positions[name] is None:
             ag_pos[name] = cp.copy(agent_positions[name])
             agent_positions[name] = None
    LOCK.release()
    for name in AGENT_NAMES:
        if not ag_pos[name] is None:
           if not agent_artists[name] is None:
              agent_artists[name].remove()
           agent_artists[name] = plt.scatter(*ag_pos[name], color=AGENT_COLOR)
    plt.draw()
    RATE.sleep()


