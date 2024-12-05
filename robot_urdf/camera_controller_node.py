import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import threading

global pos, stop_node
pos = 0.1
# Global variable to control the stopping condition
stop_node = False

class CameraControlNode(Node):
    def __init__(self):
        super().__init__('camera_controller_node')  # Node name
        self.publisher_ = self.create_publisher(Float64MultiArray, '/joint_camera_controller/commands', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)  # Timer to publish every 0.5 second
        self.get_logger().info('Camera Control Node has started.')

    def timer_callback(self):
        # If stop_node flag is set to True, do not publish anything
        global pos, stop_node
        if not stop_node:        
            # Create a Float64MultiArray message with target joint positions
            msg = Float64MultiArray()
            msg.data = [pos] 
            self.publisher_.publish(msg)
            pos = pos + 0.1

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
    global pos
    pos = 0.1  # Initialize position variable

    # Initialize rclpy and create the node
    rclpy.init(args=args)
    node = CameraControlNode()

    # Start the input listening thread
    # This is done because if we want to stop the real robot from moving
    # this is the most efficient way to do it without ctrl+c that would stop the whole program
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