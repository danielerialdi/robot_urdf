import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

global pos
pos = 0.1

class CameraControlNode(Node):
    def __init__(self):
        super().__init__('camera_controller_node')  # Node name
        self.publisher_ = self.create_publisher(Float64MultiArray, '/joint_camera_controller/commands', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)  # Timer to publish every 0.5 second
        self.get_logger().info('Camera Control Node has started.')

    def timer_callback(self):
        global pos
        # Create a Float64MultiArray message with target joint positions
        msg = Float64MultiArray()
        msg.data = [pos]  # Example: target positions for the joints
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing joint positions: {msg.data}')
        pos = pos + 0.1

def main(args=None):
    rclpy.init(args=args)
    node = CameraControlNode()
    rclpy.spin(node)  # Keep the node running until it is killed

    # Shutdown ROS 2
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
