#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import threading

def publisher():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('test', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        hello_str = "Hello world"
        rospy.loginfo("Publishing: %s", hello_str)
        pub.publish(hello_str)
        rate.sleep()

def recei(data):
    rospy.loginfo("I heard: %s", data.data)

def subscriber():
    rospy.Subscriber('chatter', String, callback=recei)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber_thread = threading.Thread(target=subscriber)
        subscriber_thread.start()

        publisher()
    except rospy.ROSInterruptException:
        pass

