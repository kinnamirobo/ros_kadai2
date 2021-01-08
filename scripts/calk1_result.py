#!/usr/bin/env python3

import subprocess
import rospy
from std_msgs.msg import Int32

def cb(message):
    if message.data == 1:
        rospy.loginfo("corect")
    elif message.data == 2:
        rospy.loginfo("incorect")

if __name__ == "__main__":
    rospy.init_node('answer')
    sub = rospy.Subscriber('cal', Int32, cb)
    rospy.spin()
