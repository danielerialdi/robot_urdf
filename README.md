To make the simulation start use the command
```
ros2 launch robot_urdf gazebo_aruco.launch.py
```
Then you have to run the following command to create the joint_camera_controller (this is necessary only to move the robotic arm, TODO put this in the launch file)
```
ros2 run controller_manager spawner.py joint_camera_controller
```
To make the robot move we have two possibility:
To move the robotic arm:
```
ros2 run robot_urdf camera_controller_node
```
To move the wheels:
```
ros2 run robot_urdf robot_controller_node
```

You can stop whenever you want the 2 nodes pressing 'q'. If you want to restart the node you have to press 'r'.


To launch the vision part you need ros2_aruco package.
Run the following commands:
```
ros2 run ros2_aruco aruco_node --ros-args --remap /image:=/robot/camera1/image_raw
```
and
```
ros2 run ros2_aruco vision_node
```

# To connect with the robot
First of all, the .bashrc should not source any ros/ros2 version. Each necessary version should be independently sourced in every terminal.

## Install ros1_bridge
If you developed your code in ros2, go into your ros2 workspace and run:
```
apt-get install ros-foxy-ros1-bridge
```
with `foxy` substituted with your ros2 distro. For the rest of the tutorial, the ROS2 distro will be assumed as `foxy`.

## Configure connection
### Robot terminal
The first terminal will be dedicated to the connection to the robot. First of all run:
```
ssh husarion@192.168.178.98
```
with `192.168.178.98` substituted with the ip address of the robot you want to connect to. For the rest of the tutorial, the ip address of the robot will be assumed as this one.
It will ask for the password, which is:
```
husarion
```
To test that the robot is working correctly, run:
```
roslaunch tutorial_pkg all.launch
```
If it returns some error, kill it and run:
```
./flash_firmware.sh
```
and try again with the previous command, which should work.

Now that the test has been done, kill the roslaunch and run:
```
export ROS_MASTER_URI=http://192.168.178.98:11311
export ROS_IP=192.168.178.98
roslaunch tutorial_pkg all.launch
``` 

Done! Now this node will keep running all the drivers of the robot, so that it can be interfaced.

## Bridge terminal
This terminal will be dedicated to the bridge between ROS1 and ROS2. Therefore, since the `ros1_bridge` is a ROS2 package, the source to your ROS2 distro is needed. For this, run:
```
source /opt/ros/foxy/setup.bash
```
Now, to export the correct ip's for the connection, run:
```
export ROS_MASTER_URI=http://192.168.178.51:11311
```
```
export ROS_IP=<pc_ip>
```
If you don't know what's your pc's ip, run `ip addr`.

Now, `ros1_bridge` can be started by running:
```
ros2 run ros1_bridge dynamic_bridge
```
If only the services are created but not the topics, kill it and rerun it with the following flag:
```
ros2 run ros1_bridge dynamic_bridge --bridge-all-topics
```

Done! Now the bridge should connect to each topic of the robot and create them one by one for ROS2. It may take a while for all the topics to be created.

## ROS2 interface terminal
To check the newly created ROS2 topics and, later, run your code on the robot, create a new terminal and source your ROS2 distro:
```
source /opt/ros/foxy/setup.bash
```
Then, you can check that all the topics have been created with:
```
ros2 topic list
```
If some topics are missing, rerunning it will update the list.

In this terminal (and other identical ones, if you need more) you can run all the nodes you developed to control the robot.
