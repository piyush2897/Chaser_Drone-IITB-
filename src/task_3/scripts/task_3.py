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


location = {
	0:(4.25, 4.05, 11),
	1:(-4.0, 3.25, 11),
	2:(-3.8, -4.2, 11),
	3:(4.25, -4.2, 11),
	4:(0, 0, 11),
} 

kpx=0.065
kdx=0.0125
kpy=0.065
kdy=0.0125
kpz=0.12
kdz=0.075

def yaw0():
	temp1= (location[0][0]-posx)/(location[0][1]-posy)
	print ""+str(posx)+""+str(posy)
	print temp1
	temp2= math.atan(temp1)
	print temp2
	temp3= math.sin(temp2/2)
	print temp3
	print Oz
	last_time=0
	lastErr=0
	while(1):
		current_time=time.time()
		time_change=current_time-last_time
		error=temp3-Oz
		dErr=(error - lastErr)/time_change
		twist.angular.z= 50*(kpz * error + kdz * dErr)
		pub_twist.publish(twist)
		lastErr=error
		last_time=current_time
		twist.linear.x=0
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
		twist.angular.x=0
		twist.angular.y=0
		pub_twist.publish(twist)
		if(Oz>temp3):
			print str(Oz)
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break

def yaw1():
	temp1= (location[1][0]-posx)/(location[1][1]-posy)
	temp2= math.atan(temp1)
	temp3= math.sin(temp2/2)
	last_time=0
	lastErr=0
	while(1):
		current_time=time.time()
		time_change=current_time-last_time
		error=temp3-Oz
		dErr=(error - lastErr)/time_change
		twist.angular.z= 50*(kpz * error + kdz * dErr)
		pub_twist.publish(twist)
		lastErr=error
		last_time=current_time
		twist.linear.x=0
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
		twist.angular.x=0
		twist.angular.y=0
		pub_twist.publish(twist)
		if(Oz>temp3):
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break

def yaw2():
	while(1):
		twist.angular.z=-5
		twist.angular.x=0
		twist.angular.y=0
		pub_twist.publish(twist)
		twist.linear.x=0
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
		if(Oz<0.001):
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break

def yaw3():
	while(1):
		twist.angular.z=-7
		twist.angular.x=0
		twist.angular.y=0
		pub_twist.publish(twist)
		twist.linear.x=0
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
		if(Oz<-0.707):
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break

def yaw4():
	temp1= (location[4][0]-posx)/(location[4][1]-posy)
	temp2= math.atan(temp1)
	temp3= math.sin((3.14-temp2)/2)
	last_time=0
	lastErr=0
	while(1):
		current_time=time.time()
		time_change=current_time-last_time
		error=temp3-Oz
		dErr=(error - lastErr)/time_change
		twist.angular.z= 110*(kpz * error + kdz * dErr)
		pub_twist.publish(twist)
		lastErr=error
		last_time=current_time
		twist.linear.x=0
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
		twist.angular.x=0
		twist.angular.y=0
		pub_twist.publish(twist)
		if(Oz>temp3):
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break

def go3():
	last_time=0
	lastErr=0
	while(1):
		current_time=time.time()
		time_change=current_time-last_time
		error=location[2][1]-posy
		dErr = (error - lastErr)/time_change
		twist.linear.x=-4.5*(kpx * error + kdx * dErr)
		pub_twist.publish(twist)
		lastErr = error
		last_time = current_time
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
		twist.angular.z=0
		twist.angular.x=0
		twist.angular.y=0
		pub_twist.publish(twist)
		if posy<location[2][1]+0.05 and posy>location[2][1]-0.05:
			print "AIM 3 = " + str(posx) + " "+ str(posy) +" "+str(posz)
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break

def go4():
	last_time=0
	lastErr=0
	while(1):
		current_time=time.time()
		time_change=current_time-last_time
		error=location[3][0]-posx
		dErr = (error - lastErr)/time_change
		twist.linear.x=4*(kpx * error + kdx * dErr)
		pub_twist.publish(twist)
		lastErr = error
		last_time = current_time
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
		twist.angular.z=0
		twist.angular.x=0
		twist.angular.y=0
		pub_twist.publish(twist)
		if posx<location[3][0]+0.05 and posx>location[3][0]-0.05:
			print "AIM 4 = " + str(posx) + " "+ str(posy) +" "+str(posz)
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break

def go5():
	last_time=0
	lastErr=0
	while(1):
		current_time=time.time()
		time_change=current_time-last_time
		error=location[4][0]-posx
		dErr = (error - lastErr)/time_change
		twist.linear.x=-5*(kpx * error + kdx * dErr)
		pub_twist.publish(twist)
		lastErr = error
		last_time = current_time
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
		twist.angular.z=0
		twist.angular.x=0
		twist.angular.y=0
		pub_twist.publish(twist)
		if posx<location[4][0]+0.05 and posx>location[4][0]-0.05:
			print "AIM 5 = " + str(posx) + " "+ str(posy) +" 10.8529949188"
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break



def go1():
    last_time=0
    lastErr=0
    while(1):
    	current_time=time.time()
    	time_change=current_time-last_time
    	error=location[0][1]-posy
    	dErr = (error - lastErr)/time_change
    	twist.linear.x= -7*(kpx * error + kdx * dErr)
    	pub_twist.publish(twist)
    	lastErr = error
    	last_time = current_time
    	twist.linear.y=0
    	twist.linear.z=0
    	pub_twist.publish(twist)
    	twist.angular.x=0
    	twist.angular.y=0
    	twist.angular.z=0
    	pub_twist.publish(twist)
    	if posy<location[0][1]+0.01 and posy>location[0][1]-0.01:
    		print "AIM 1 = " + str(posx) + " "+ str(posy) +" "+str(posz)
    		twist.linear.x=0
    		twist.linear.y=0
    		twist.linear.z=0
    		pub_twist.publish(twist)
    		twist.angular.x=0
    		twist.angular.y=0
    		twist.angular.z=0
    		pub_twist.publish(twist)
    		break

def zc():
    last_time=0
    lastErr=0
    while(1):
    	current_time=time.time()
    	time_change=current_time-last_time
    	error=location[0][2]-posz
    	dErr = (error - lastErr)/time_change
    	twist.linear.z= -(kpz * error + kdz * dErr)
    	pub_twist.publish(twist)
    	lastErr = error
    	last_time = current_time
    	twist.linear.x=0
    	twist.linear.y=0
    	pub_twist.publish(twist)
    	if posz<location[0][2]+0.8 and posz>location[0][2]-0.3:
    		print "position of X Y Z = " + str(posx) + " "+ str(posy) +" "+str(posz)
    		twist.linear.z=0
    		pub_twist.publish(twist)
    		break

def go2():
	last_time=0
	lastErr=0
	while(1):
		current_time=time.time()
		time_change=current_time-last_time
		error=location[1][0]-posx
		dErr = (error - lastErr)/time_change
		twist.linear.x=-5*(kpx * error + kdx * dErr)
		pub_twist.publish(twist)
		lastErr = error
		last_time = current_time
		twist.linear.y=0
		twist.linear.z=0
		pub_twist.publish(twist)
			print "AIM 2 = " + str(posx) + " "+ str(posy) +" "+str(posz)
			twist.linear.x=0
			twist.linear.y=0
			twist.linear.z=0
			pub_twist.publish(twist)
			twist.angular.z=0
			twist.angular.x=0
			twist.angular.y=0
			pub_twist.publish(twist)
			break




status_Of_drone = 0

def subscribe_and_Publish_Topics():
	rospy.init_node("subscribe_and_Publish_Topics")
	rospy.Subscriber("/whycon/poses",PoseArray,getPositions)
	rospy.Subscriber("/ardrone/navdata",Navdata,getFlightStatus)
	rospy.Subscriber("/ardrone/imu",Imu,getOrientation)       


def getPositions(data):	
	global posx ,posy , posz
	posx =  data.poses[0].position.x
	posy =  data.poses[0].position.y
	posz =  data.poses[0].position.z	

def getOrientation(orient):
	global Ox,Oy,Oz,Ow
	Ox = orient.orientation.x
	Oy = orient.orientation.y
	Oz = orient.orientation.z
	Ow=0		

def getFlightStatus(status):
	global status_Of_drone
	status_Of_drone = status.state


if __name__ == '__main__':
	subscribe_and_Publish_Topics()
	pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=100)
	pub_empty_takeoff = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=100)
	pub_empty_landing = rospy.Publisher('/ardrone/land', Empty,queue_size=100)
	pub_reset = rospy.Publisher('/ardrone/reset',Empty,queue_size=100)
	twist = Twist()

	while(1):
		while status_Of_drone == 0 or status_Of_drone == 2:
			pub_empty_takeoff.publish(Empty())
			time.sleep(2)
			if status_Of_drone == 3 or status_Of_drone == 8 :
				print "Drone in Air"
				break
		time.sleep(2)		
		go1()
		time.sleep(0.5)
		yaw1()
		time.sleep(0.5)
		go2()
		time.sleep(0.5)
		yaw2()
		time.sleep(0.5)
		go3()
		time.sleep(0.5)
		yaw3()
		time.sleep(0.5)
		go4()
		time.sleep(0.5)
		yaw4()
		time.sleep(0.5)
		go5()
		#print status_Of_drone
		if status_Of_drone == 3 or status_Of_drone == 8 :
			while(1):
				pub_empty_landing.publish(Empty())


   
	   







				    current_time=time.time()
				    time_change=current_time-last_timeY
				    errorY=location[0][1]-posy
				    dErrY = (errorY - lastErrY)/time_change
				    self.cmd.rcThrottle =1500
				    self.cmd.rcPitch =1500
				    self.cmd.rcYaw =1500
				    self.cmd.rcRoll = 1500 + 250 * (kpy * errorY + kdy * dErrY)
				    self.command_pub.publish(self.cmd)
				    print 1500 + 1095*(kpy * errorY + kdy * dErrY)
				    lastErrY = errorY
			    	last_timeY = current_time
			    	current_time=time.time()
			    	time_change=current_time-last_timeX
			    	errorX=location[0][0]-posx
			    	dErrX = (errorX - lastErrX)/time_changes
			    	self.cmd.rcThrottle =1500
			    	self.cmd.rcRoll =1500
			    	self.cmd.rcYaw =1500
			    	#self.cmd.rcPitch = 1500 + 1095 * (kpx * errorX + kdx * dErrX)
			    	#self.command_pub.publish(self.cmd)
			    	print 1500 + 1095*(kpx * errorX + kdx * dErrX)
			    	lastErrX = errorX
			    	last_timeX = current_time 
			    	  

			    	if posz>location[0][2]:
		    	while 1:
			    	current_time=time.time()
			    	time_change=current_time-last_timeZ
			    	errorZ=location[0][2]-posz
			    	dErrZ = (errorZ - lastErrZ)/time_change
			    	self.cmd.rcRoll =1500
			    	self.cmd.rcPitch =1500
			    	self.cmd.rcYaw =1500
			    	self.cmd.rcThrottle = 1700 - 500*(kpz * errorZ + kdz * dErrZ)
			    	self.command_pub.publish(self.cmd)
			    	print 1700 - 500*(kpz * errorZ + kdz * dErrZ)
			    	lastErrZ = errorZ
		    		last_timeZ = current_time
		    		if posz<location[0][2]:
			    		print "position of X Y Z = " + str(posx) + " "+ str(posy) +" "+str(posz)
			    		#self.reset()
			    		break 		