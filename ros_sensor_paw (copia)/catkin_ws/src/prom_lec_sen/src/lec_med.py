#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

def pose(pose_med):
    pub = rospy.Publisher('medicion_contacto', Pose2D, queue_size=10)
    rospy.init_node('medicion_cont', anonymous=True)
    rate = rospy.Rate(50)
    cont=0
    while not rospy.is_shutdown():
        cont+=1
        
        
        pose=Pose2D()
        pose.x= pose_med.x
        pose.y= pose_med.y
        pose.theta= pose_med.theta
        rospy.loginfo(pose)
        pub.publish(pose)
        rate.sleep()

def callback(data):
    pose_med=data.data

def listener():
    rospy.init_node('leer__med_ard', anonymous=True)
    rospy.Subscriber("medicion_cont_paw", Pose2D, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
