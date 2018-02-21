#!/usr/bin/env python
from whycon.srv import SetNumberOfTargets

target = 2
thresh_value = 0

rospy.wait_for_service('whycon/reset')
try:
	target_value = rospy.ServiceProxy('whycon/reset', SetNumberOfTargets)
	resp1 = target_value(target,thresh_value)
except rospy.ServiceException, e:
	print "Service call failed: %s"%e