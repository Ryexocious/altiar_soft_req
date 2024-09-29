#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
def move_circle(pub):
    vel_msg = Twist()
    vel_msg.linear.x = 2.0
    vel_msg.angular.z = 2.0
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

def move_square(pub):
    vel_msg = Twist()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        vel_msg.linear.x = 2.0
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)
        rospy.sleep(2)

        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 3.14/2
        pub.publish(vel_msg)
        rospy.sleep(2)

def move_spiral(pub):
    vel_msg = Twist()
    rate = rospy.Rate(10)
    r = 1.0
    while not rospy.is_shutdown():
        vel_msg.linear.x = r
        vel_msg.angular.z = 1.0
        pub.publish(vel_msg)
        r += 0.1
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('shapes')
    rospy.loginfo('node start')

    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    print("Enter 'A' for circle, 'B' for square, 'C' for spiral:")
    choice = input().strip().upper()

    if choice == 'A':
        move_circle(pub)
    elif choice == 'B':
        move_square(pub)
    elif choice == 'C':
        move_spiral(pub)