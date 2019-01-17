#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
import math
import time
import numpy as np 

distance = 0


def echo_callback(echo_data):
    global distance
    distance = echo_data.range
    #print(distance)


if __name__ == '__main__':
    
    #init new a node and give it a name
    rospy.init_node('echo_node', anonymous=True)
    #subscribe to the topic /scan. 
    rospy.Subscriber("/ultrasound_range", Range, echo_callback)
    cmd_vel_topic='/cmd_vel_mux/input/teleop'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    soundhandle = SoundClient()
    time.sleep(2)

    vel_msg = Twist()

    while True:
        if 100.0 < distance < 150.0:
            vel_msg.linear.x = -0.05
            velocity_publisher.publish(vel_msg)
            print("Beep sound at interval promotional to the distance to obstacle")
            soundhandle.playWave('say-beep.wav')
            time.sleep(math.tanh((distance/1000*1.0 + 0.4)))
        elif 70.0 < distance < 100.0: 
            vel_msg.linear.x = -0.04
            velocity_publisher.publish(vel_msg)
            print("Continuous beep")
            soundhandle.playWave('say-beep.wav')
            time.sleep(0.3)
        elif distance < 70.0: 
            vel_msg.linear.x = 0.0
            velocity_publisher.publish(vel_msg)
            print("Stop")
        else:
            vel_msg.linear.x = -0.1
            velocity_publisher.publish(vel_msg)
            print("Not Started") 




    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()