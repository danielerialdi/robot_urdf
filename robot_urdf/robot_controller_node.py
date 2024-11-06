import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotControlNode(Node):
    def __init__(self):
        super().__init__('robot_controller_node')  # Node name
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)  # Timer to publish every 0.5 second
        self.get_logger().info('Robot Control Node has started.')

    def timer_callback(self):
        msg = Twist()
        # Set linear and angular velocities here
        msg.linear.x = 0.0  # Linear velocity (m/s)
        msg.angular.z = 1.0  # Angular velocity (rad/s)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotControlNode()
    rclpy.spin(node)  # Keep the node running until it is killed

    # Shutdown ROS 2
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
