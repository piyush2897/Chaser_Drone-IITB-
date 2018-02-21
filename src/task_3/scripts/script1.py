#!/usr/bin/env python
from plutodrone.srv import *
from plutodrone.msg import *
from std_msgs.msg import Int16
import rospy

import roslib
import time
import sys
import math

from std_msgs.msg import Empty
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseArray, Pose
from ardrone_autonomy.msg import Navdata
from sensor_msgs.msg import Imu

import sys, select, termios, tty

kpx=25  #0.065
kdx=30  #0.0125
kpy=25  #0.065
kdy=30  #0.0125
kpz=75 #0.12
kdz=3  #0.075

def getPositions(data):	
	global posx ,posy , posz
	posx =  data.poses[0].position.x
	posy =  data.poses[0].position.y
	posz =  data.poses[0].position.z

class send_data():
	def __init__(self):
		rospy.init_node('drone_server')
		self.command_pub = rospy.Publisher('/drone_command', PlutoMsg, queue_size=1)
		rospy.Subscriber('/input_key', Int16, self.indentify_key )

		self.key_value =0
		self.cmd = PlutoMsg()
		self.cmd.rcRoll =1500
		self.cmd.rcPitch = 1500
		self.cmd.rcYaw =1500
		self.cmd.rcThrottle =1500
		self.cmd.rcAUX1 =1500
		self.cmd.rcAUX2 =1500
		self.cmd.rcAUX3 =1500
		self.cmd.rcAUX4 =1000
		
	def arm(self):
		self.cmd.rcRoll=1500
		self.cmd.rcYaw=1500
		self.cmd.rcPitch =1500
		self.cmd.rcThrottle =1000
		self.cmd.rcAUX4 =1500
		self.command_pub.publish(self.cmd)
		rospy.sleep(.1)

	def disarm(self):
		self.cmd.rcThrottle =1300
		self.cmd.rcAUX4 = 1200
		self.command_pub.publish(self.cmd)
		rospy.sleep(1)
	
	def indentify_key(self, msg):
		self.key_value = msg.data

	def forward(self):
		self.cmd.rcPitch =1600
		self.command_pub.publish(self.cmd)

	def backward(self):
		self.cmd.rcPitch =1400
		self.command_pub.publish(self.cmd)

	def left(self):
		self.cmd.rcRoll =1600
		self.command_pub.publish(self.cmd)	

	def right(self):
		self.cmd.rcRoll =1400
		self.command_pub.publish(self.cmd)

	def reset(self):
		self.cmd.rcRoll =1500
		self.cmd.rcThrottle =1500
		self.cmd.rcPitch =1500
		self.cmd.rcYaw = 1500
		self.command_pub.publish(self.cmd)

	def increase_height(self):
		self.cmd.rcThrottle = 2000
		self.command_pub.publish(self.cmd)

	def decrease_height(self):
		self.cmd.rcThrottle =1400
		self.command_pub.publish(self.cmd)

	def pid(self):
		while 1:
			print "PID"
			lasttimex=0
			lasttimey=0
			lasttimez=0
			lasterrx =0
			lasterry =0
			lasterrz =0
			print "a"
			if posy > 0.2 or posy < -0.2 :
				print "posy"
				while True:
					curr_time   = time.time()
					timechangey = curr_time - lasttimey
					errory      = -posy
					derry       = (errory - lasterry)/timechangey
					self.cmd.rcThrottle =1500
					self.cmd.rcRoll     =1500 + 500*(kpy*errory+kdy*derry)
					self.cmd.rcYaw 	    =1500
					self.cmd.rcPitch    =1500
					self.command_pub.publish(self.cmd)
					print "roll = ",
					print 1500 + 500*(kpy*errory+kdy*derry)
					lasterry = errory
					lasttimey= curr_time
					if (posy < 0.2 and posy > -0.2):
						break

			elif posx > 0.2 or posx < -0.2 :
				print "posx"
				while True:
					curr_time   = time.time()
					timechangex = curr_time - lasttimex
					errorx      = -posx
					derrx       = (errorx - lasterrx)/timechangex
					self.cmd.rcThrottle =1500
					self.cmd.rcRoll     =1500
					self.cmd.rcYaw 		=1500
					self.cmd.rcPitch    =1500 + 500*(kpx*errorx+kdx*derrx)
					self.command_pub.publish(self.cmd)	
					print "Pitch = ",
					print  1500 + 500*(kpx*errorx+kdx*derrx)
					lasterrx = errorx
					lasttimex= curr_time
					if (posx < 0.2 and posx > -0.2):
						 break

			elif posz > 27 :
				print "posz"
				while True:
					curr_time   = time.time()
					timechangez = curr_time - lasttimez
					errorz      = 27-posz
					derrz       = (errorz - lasterrz)/timechangez
					self.cmd.rcThrottle =round(1500 - ((kpz*errorz)+(kdz*derrz)))
					self.cmd.rcRoll    =1500
					self.cmd.rcYaw 	   =1500
					self.cmd.rcPitch   =1500
					self.command_pub.publish(self.cmd)	
					print "Throttle = ",
					print 1500 - (kpz*errorz+kdz*derrz)
					lasterrz = errorz
					lasttimez= curr_time
			    	if (posz < 27):
			    		break
		

	def control_drone(self):
		# print "a"
		while 1 :
			if self.key_value == 70:
				self.disarm()
			elif self.key_value == 10:	
				self.pid()
			elif self.key_value == 50:
				self.arm()
			self.command_pub.publish(self.cmd)


if __name__ == '__main__':
	while not rospy.is_shutdown():
		rospy.Subscriber("/whycon/poses",PoseArray,getPositions)
		test = send_data()
		test.control_drone()
		rospy.spin()
		sys.exit(1)


