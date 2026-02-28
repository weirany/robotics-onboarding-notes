import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.srv = self.create_service(AddTwoInts, "add_two_ints", self.add_callback)
        self.get_logger().info("Service [add_two_ints] ready.")

    def add_callback(self, request, response):
        import time
        time.sleep(5)
        a = request.a
        b = request.b
        response.sum = a + b
        self.get_logger().info(f"Request: a={a}, b={b} -> sum={response.sum}")
        return response


def main():
    rclpy.init()
    node = AddTwoIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
