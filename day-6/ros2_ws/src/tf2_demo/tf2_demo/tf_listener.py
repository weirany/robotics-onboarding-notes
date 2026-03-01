#!/usr/bin/env python3
import math

import rclpy
from rclpy.node import Node

from tf2_ros import Buffer, TransformListener


def quat_to_yaw(qx, qy, qz, qw) -> float:
    """Extract yaw from quaternion assuming Z-up (planar)."""
    # yaw (z-axis rotation)
    siny_cosp = 2.0 * (qw * qz + qx * qy)
    cosy_cosp = 1.0 - 2.0 * (qy * qy + qz * qz)
    return math.atan2(siny_cosp, cosy_cosp)


class SimpleTfListener(Node):
    def __init__(self):
        super().__init__("simple_tf_listener")
        self.buffer = Buffer()
        self.listener = TransformListener(self.buffer, self)

        self.timer = self.create_timer(0.5, self.on_timer)
        self.get_logger().info("Listening TF: odom -> base_link (print pose)")

    def on_timer(self):
        try:
            tf = self.buffer.lookup_transform("odom", "base_link", rclpy.time.Time())
            tx = tf.transform.translation.x
            ty = tf.transform.translation.y
            q = tf.transform.rotation
            yaw = quat_to_yaw(q.x, q.y, q.z, q.w)
            self.get_logger().info(f"base_link in odom: x={tx:.2f}, y={ty:.2f}, yaw={yaw:.2f} rad")
        except Exception as e:
            self.get_logger().warn(f"TF lookup failed: {e}")


def main():
    rclpy.init()
    node = SimpleTfListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()