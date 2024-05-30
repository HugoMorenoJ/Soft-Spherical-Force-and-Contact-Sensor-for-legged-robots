#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

historyx = []
historyy = []

def callback(pose_med):
    pub = rospy.Publisher('med_corr_sen', Pose2D, queue_size=10)
    pose=Pose2D()
    global historyx, historyy
    historyx.append(pose_med.x)
    historyy.append(pose_med.y)
    if len(historyx) > 10:
    	historyx = historyx[-10:]
    if len(historyy) > 10:
        historyy = historyy[-10:]
    averagex = (sum(historyx)-max(historyx)-min(historyx))/ (float(len(historyx))-2)
    averagey = (sum(historyy)-max(historyy)-min(historyy))/ (float(len(historyy))-2)


    
    
    pose.x= averagex 
    pose.y= averagey 
    pose.theta= 0


    rospy.loginfo(pose)
    pub.publish(pose)
    #rate.sleep()
    #pose(pose_med)



def listener():
    rospy.init_node('leer_sen', anonymous=True)
    rospy.Subscriber("sensor_contacto", Pose2D, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
