#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32

if __name__ == "__main__":
    rospy.init_node('question')
    pub = rospy.Publisher('cal', Int32, queue_size=1)
    while not rospy.is_shutdown():
        a = random.randint(1,100)
        b = random.randint(1,a)
        print('Choose between addition, subtraction, multiplication and division')
        print('+:1, -:2, *:3 ')
        i = int(input())
        if i == 1:
            print('%d + %d = ?' %(a, b))
            n = input('Ansewr Enter>')
            if n.isdigit():
                n = int(n)
                if n == (a + b):
                    pub.publish(1)
                elif n != (a + b):
                    pub.publish(2)
            else:
                pub.publish(0)
                break

        elif i == 2:
            print('%d - %d = ?' %(a, b))
            n = input('Ansewr Enter>')
            if n.isdigit():
                n = int(n)
                if n == (a - b):
                    pub.publish(1)
                elif n != (a - b):
                    pub.publish(2)
            else:
                pub.publish(0)
                break

        elif i == 3:
            print('%d * %d = ?' %(a, b))
            n = input('Ansewr Enter>')
            if n.isdigit():
                n = int(n)
                if n == (a * b):
                    pub.publish(1)
                elif n != (a * b):
                    pub.publish(2)
            else:
                pub.publish(0)
                break

        else:
            print("era-")
