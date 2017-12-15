#!/usr/bin/python

import rospy as rp
import geomtwo.msg as gms
import geomtwo.impl as gmi
import threading as thd
from std_msgs.msg import Float32


#Initial position
position = rp.get_param('initial_position')[0]
pos = gmi.Versor(position)

LOCK = thd.Lock()

#Velocity
velocity = None


rp.init_node('simulator')

FREQUENCY = 10e1
RATE = rp.Rate(FREQUENCY)
TIME_STEP = 2.0/FREQUENCY

def cmdvel_callback(msg):
    global velocity
    LOCK.acquire()
    velocity = msg
    LOCK.release()
rp.Subscriber(
    name = 'cmdvel',   
    data_class = Float32,
    callback = cmdvel_callback,
    queue_size = 10)

start = False

#Publisher
pub = rp.Publisher(
        name = 'position',
        data_class = gms.Vector,
        queue_size = 10)



while not rp.is_shutdown() and not start:
    LOCK.acquire()
    if not velocity is None:
      start = True
    LOCK.release()
    #Initial position publishing              
    pub.publish(pos.serialize())
    RATE.sleep()

while not rp.is_shutdown():
    LOCK.acquire()
    #Position
    pos = pos.rotate(velocity.data*TIME_STEP)
    LOCK.release()
    #Position publishing
    pub.publish(pos.serialize())

    RATE.sleep()



 


