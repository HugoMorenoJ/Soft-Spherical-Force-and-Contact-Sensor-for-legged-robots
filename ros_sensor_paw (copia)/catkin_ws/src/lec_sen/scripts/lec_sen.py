#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D


def callback(pose_med):
    pub = rospy.Publisher('sensor_contacto', Pose2D, queue_size=10)
    pose=Pose2D()
    pose.x= (pose_med.x - 430)*2.18
    pose.y= (-(pose_med.y -515)) *3.6
    pose.theta=(pose_med.y - 9041815)*0.009
    rospy.loginfo(pose)
    pub.publish(pose)
    #rate.sleep()


def listener():
    rospy.init_node('leer_cont_ard', anonymous=True)
    rospy.Subscriber("contacto_paw", Pose2D, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
