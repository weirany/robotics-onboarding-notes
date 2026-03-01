#!/usr/bin/env python3
import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


def yaw_to_quat(yaw: float):
    """Convert yaw (Z rotation) to quaternion (x,y,z,w)."""
    half = yaw * 0.5
    return (0.0, 0.0, math.sin(half), math.cos(half))


class OdomToBaseBroadcaster(Node):
    def __init__(self):
        super().__init__("odom_to_base_broadcaster")
        self.br = TransformBroadcaster(self)

        # publish at 20Hz
        self.timer = self.create_timer(0.05, self.on_timer)

        # motion params
        self.radius = 1.0  # meters
        self.omega = 0.5   # rad/s

        self.get_logger().info("Publishing dynamic TF: odom -> base_link")

    def on_timer(self):
        now = self.get_clock().now()
        t = now.nanoseconds * 1e-9

        x = self.radius * math.cos(self.omega * t)
        y = self.radius * math.sin(self.omega * t)
        yaw = self.omega * t  # facing direction changes over time

        tf_msg = TransformStamped()
        tf_msg.header.stamp = now.to_msg()
        tf_msg.header.frame_id = "odom"
        tf_msg.child_frame_id = "base_link"

        tf_msg.transform.translation.x = float(x)
        tf_msg.transform.translation.y = float(y)
        tf_msg.transform.translation.z = 0.0

        qx, qy, qz, qw = yaw_to_quat(yaw)
        tf_msg.transform.rotation.x = qx
        tf_msg.transform.rotation.y = qy
        tf_msg.transform.rotation.z = qz
        tf_msg.transform.rotation.w = qw

        self.br.sendTransform(tf_msg)


def main():
    rclpy.init()
    node = OdomToBaseBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()