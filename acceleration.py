# -*- coding: utf-8 -*-

import rospy
from geometry_msgs import TwistStamped
import math

previous_velocity_x = 0.0
previous_velocity_y = 0.0
previous_velocity_z = 0.0
previous_time = rospy.get_rostime().to_sec()


def velocity_to_acceleration(pose):
    global previous_velocity_x, previous_velocity_y, previous_velocity_z, previous_time
    acceleration_x = (pose.twist.linear.x - previous_velocity_x) / (rospy.get_rostime().to_sec() - previous_time)
    acceleration_y = (pose.twist.linear.y - previous_velocity_y) / (rospy.get_rostime().to_sec() - previous_time)
    acceleration_z = (pose.twist.linear.z - previous_velocity_z) / (rospy.get_rostime().to_sec() - previous_time)
    overall_acceleration = math.sqrt(acceleration_x**2 + acceleration_y**2 + acceleration_z**2)
    previous_velocity_x = pose.twist.linear.x
    previous_velocity_y = pose.twist.linear.y
    previous_velocity_z = pose.twist.linear.z
    previous_time = rospy.get_rostime().to_sec()
    print 'x:', acceleration_x, 'y:', acceleration_y, 'z:', acceleration_z, 'overall:', overall_acceleration


def listener():
    rospy.init_node("acceleration")
    rospy.Subscribe("/mavros/local_position/velocity", TwistStamped, velocity_update)
    rospy.spin()


if __name__ == '__main__':
    listener()
