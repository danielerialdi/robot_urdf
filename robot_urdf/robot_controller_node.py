import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import threading
import time
# Global variable to control the stopping condition
stop_node = False

class RobotControlNode(Node):
    def __init__(self):
        super().__init__('robot_controller_node')  # Node name
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)  # Timer to publish every 0.5 second
        self.get_logger().info('Robot Control Node has started.')

    def timer_callback(self):
        msg = Twist()
        if stop_node:
            msg.linear.x = 0.0  # Linear velocity (m/s)
            msg.angular.z = 0.0  # Angular velocity (rad/s)
            self.publisher_.publish(msg)
        else:
            # Set linear and angular velocities here
            msg.linear.x = 0.0  # Linear velocity (m/s)
            msg.angular.z = 1.0  # Angular velocity (rad/s)
            self.publisher_.publish(msg)


# Function to handle user input and stop the node
def input_thread():
    global stop_node
    while True:
        user_input = input("Press 'q' to stop the node, 'r' to restart it: ")
        if user_input == 'q':
            stop_node = True
            print("Stopping the node...")
        elif user_input == 'r' and stop_node:
            stop_node = False
            print("Restarting the node...")


def main(args=None):
    # Initialize rclpy and create the node
    rclpy.init(args=args)
    node = RobotControlNode()

    # Start the input listening thread
    thread = threading.Thread(target=input_thread)
    thread.daemon = True  # Daemonize the thread to allow it to exit when the program exits
    thread.start()

    # Keep the node running until stop_node is True
    while rclpy.ok():
        rclpy.spin_once(node)

    # Shutdown ROS 2 and clean up
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
