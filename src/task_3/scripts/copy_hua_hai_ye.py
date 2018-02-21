# Team Id : 1943
# Author List : Piyush ,Shivam, Rohit ,Akash
# FileName: Script2.py 
# Theme: 1943
# Function : getPositions,arm,indentify_key,pid,control_drone
# Global Variables: posx,posy,posz,kpx,kpy,kpz,kdx,kdy,kdz,kix,kiy,kiz 

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

#Tuning Constants for PID
kpx=20
kix=1
kdx=12
kpy=20
kiy=1
kdy=12
kpz=60
kiz=0
kdz=2

# Function Name: getPositions
# Input: data from the camera to find x,y,z
# Output: x,y,z co-ordinates of drone w.r.t camera
# Logic: it extracts x,y,z co-ordinates from the structure PoseArray
# Example Call: rospy.Subscriber("/whycon/poses",PoseArray,getPositions)


def getPositions(data):	
	#posx,posy,posz : current position of drone in x,y,z axis 
	global posx ,posy , posz
	posx =  data.poses[0].position.x
	posy =  data.poses[0].position.y
	posz =  data.poses[0].position.z

class send_data():

	#constructor Function called automatically when object is created 
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

# Function Name: arm
# Input: no input but called with the object of class created initially 
# Output: it starts the wings of drone
# Logic: it publishes desired value of throttle, yaw,pitch and roll to the drone
# Example Call: self.arm()		
		
	def arm(self):
		self.cmd.rcRoll=1500
		self.cmd.rcYaw=1500
		self.cmd.rcPitch =1500
		self.cmd.rcThrottle =1000
		self.cmd.rcAUX4 =1500
		self.command_pub.publish(self.cmd)
		rospy.sleep(.1)

# Function Name: identify_key
# Input: called with the help of constructor with "msg"<input> from keyboard
# Output: helps in giving instruction from keyboard to drone
# Logic: the message from keyboard stored in msg variable is given to keyvalue which takes appropriate action
# Example Call: rospy.Subscriber('/input_key', Int16, self.indentify_key )
	
	def indentify_key(self, msg):
		self.key_value = msg.data

# Function Name: pid
# Input: call via object and has access to current position of drone in x,y,z axis
# Output: keeps the drone in desired postion
# Logic: publishes throttle,roll,pitch,yaw accordingly so that it stays in a desired location.
# Example Call: self.pid()

	def pid(self):
		print "PID"
		lasttimex=time.time()-0.0010001
		lasttimey=time.time()-0.0010001
		lasttimez=time.time()-0.0010001
		lasterrx =0
		lasterry =0
		lasterrz =0
		ierrory  =0
		ierrorx  =0
		ierrorz  =0
		while 1:
			#applying PID in y axis
			curr_time   = time.time()
			timechangey = curr_time - lasttimey
			errory      = -posy
			ierrory		= ierrory + (errory)*timechangey
			derry       = (errory - lasterry)/timechangey
			print "roll = ",
			print 1500 + (kpy*errory+ kiy*ierrory  +kdy*derry)
			roll = 1500 + (kpy*errory+ kiy*ierrory  +kdy*derry)
			lasterry = errory
			lasttimey= curr_time

			#applying PID in x axis
			curr_time   = time.time()
			timechangex = curr_time - lasttimex
			errorx      = -posx
			ierrorx		= ierrorx + (errorx)*timechangex
			derrx       = (errorx - lasterrx)/timechangex	
			print "Pitch = ",
			print  1500 + (kpx*errorx+  kix*ierrorx +kdx*derrx)
			pitch = 1500 + (kpx*errorx+  kix*ierrorx +kdx*derrx)
			lasterrx = errorx
			lasttimex= curr_time

			#applying PID in z axis
			curr_time   = time.time()
			timechangez = curr_time - lasttimez
			errorz      = 27-posz
			ierrorz     = ierrorz + (errorz)*timechangez
			derrz       = (errorz - lasterrz)/timechangez
			print "Throttle = ",
			Throttle = 1500 - (kpz*errorz+ kiz*ierrorz +kdz*derrz)
			if Throttle > 2000:  #at max value of throttle can be 2000
				Throttle = 2000
			print Throttle	
			lasterrz = errorz
			lasttimez= curr_time

			self.cmd.rcThrottle =Throttle
			self.cmd.rcRoll     =roll
			self.cmd.rcYaw 	    =1500
			self.cmd.rcPitch    =pitch
			rospy.sleep(0.01)
			self.command_pub.publish(self.cmd)	

# Function Name: control_drone()
# Input: keyvalues i.e input from the keyboard.
# Output: its decides whether to arm, disarm or fly the drone accordingly.
# Logic: simple use of while and if can do the desired function.
# Example Call: <object_name>.control_drone()		

	def control_drone(self):
		while 1 :
			if self.key_value == 70:
				self.disarm()
			if self.key_value == 10:	
				self.pid()
			if self.key_value == 50:
				self.arm()
			self.command_pub.publish(self.cmd)

#main Function
if __name__ == '__main__':
	while not rospy.is_shutdown():
		rospy.Subscriber("/whycon/poses",PoseArray,getPositions)
		test = send_data()  #object created for the class send data
		test.control_drone()
		rospy.spin()
		sys.exit(1)