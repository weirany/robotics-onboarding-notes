import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleListener(Node):
    def __init__(self):
        super().__init__('simple_listener')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self._callback,
            10
        )
        self.get_logger().info("SimpleListener started. Subscribing to topic 'chatter'.")

    def _callback(self, msg: String):
        self.get_logger().info(f"Received: {msg.data}")

def main():
    rclpy.init()
    node = SimpleListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()