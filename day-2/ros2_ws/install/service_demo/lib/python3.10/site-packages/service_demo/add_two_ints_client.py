import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.cli = self.create_client(AddTwoInts, "add_two_ints")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting...")

        self.req = AddTwoInts.Request()

    def send_request(self, a: int, b: int):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    if len(sys.argv) != 3:
        print("Usage: ros2 run service_demo add_two_ints_client A B")
        return

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    node = AddTwoIntsClient()
    future = node.send_request(a, b)

    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        node.get_logger().info(f"Result: {a} + {b} = {future.result().sum}")
    else:
        node.get_logger().error("Service call failed.")

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
