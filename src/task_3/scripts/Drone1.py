#!/usr/bin/env python
import roslib
import rospy
import time
import sys
import math

from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseArray, Pose
from ardrone_autonomy.msg import Navdata
from sensor_msgs.msg import Imu

import sys, select, termios, tty

status_Of_drone = 0

def subscribe_and_Publish_Topics():
	rospy.init_node("subscribe_and_Publish_Topics")
	rospy.Subscriber("/whycon/poses",PoseArray,getPositions) 

def getPositions(data):	
	global posx ,posy , posz
	posx =  data.poses[0].position.x
	posy =  data.poses[0].position.y
	posz =  data.poses[0].position.z

if __name__ == '__main__':
	subscribe_and_Publish_Topics()
	pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=100)
	pub_reset = rospy.Publisher('/ardrone/reset',Empty,queue_size=100)
	twist = Twist()
	while(1):
		print "AIM 2 = " + str(posx) + " "+ str(posy) +" "+str(posz)