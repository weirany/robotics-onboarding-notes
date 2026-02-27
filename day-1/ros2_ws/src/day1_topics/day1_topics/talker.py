import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleTalker(Node):
    def __init__(self):
        super().__init__('simple_talker')

        # 参数：发布频率 Hz、消息前缀
        self.declare_parameter('hz', 2.0)
        self.declare_parameter('prefix', 'hello')

        self.publisher_ = self.create_publisher(String, 'chatter', 10)

        self.count = 0
        self._reset_timer()

        self.get_logger().info("SimpleTalker started. Publishing on topic 'chatter'.")

    def _reset_timer(self):
        hz = float(self.get_parameter('hz').value)
        period = 1.0 / hz if hz > 0 else 0.5
        if hasattr(self, 'timer'):
            self.timer.cancel()
        self.timer = self.create_timer(period, self._on_timer)

    def _on_timer(self):
        prefix = str(self.get_parameter('prefix').value)
        msg = String()
        msg.data = f"{prefix} #{self.count}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.count += 1

def main():
    rclpy.init()
    node = SimpleTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()