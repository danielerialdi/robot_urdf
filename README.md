# robot_urdf

This repository contains the Control Package for the first assignment of the Experimental Robotics Laboratory course at the Robotics Engineering Master by UniGE.
The authors are:
- Valentina Condorelli, 4945679;
- Annika Delucchi, 4975984;
- Ramona Ferrari, 4944096;
- Daniele Rialdi, 4964038.

The package was initially forked by the Professor's repository, to which we added the following files:
- `aruco_5.world`, to spawn the requested 5 Aruco markers in a circle
- `camera_controller_node.py`, to rotate the camera, which was raised and placed on a new vertical link
- `robot_controller_node.py`, to rotate the robot

## Assignment
The assignment required to:
- spawn the robot in Gazebo, surrounded by 5 Aruco markers arranged in a circle;
- implement a routine that starts finding the marker with the lowest ID, and then finds all markers in order;
- each time a marker is found, a new image is published on a custom topic with a circle around the marker found;
- implement the same behaviour with two different nodes: in the first one, the whole robot moves; in the second one, you find the markers by only moving the camera.

To develop it, other than adding the new files mentioned above, we modified some of the already provided files

Additionally, this behaviour could be tested also on real robots.

### aruco_5.world
In order to generate the required world with 5 aruco markers around the robot, we created a new world in Gazebo, added 5 aruco markers (from id 20 to id 24, in random order) in a circle and saved the file in the `worlds` folder of our repo.

### camera_controller_node.py
This node controls the position of the camera link, by making it rotate by a fixed position offset (0.1) every 0.5 seconds. Moreover, we added multithreading in order to be able to stop the node by pressing `q` without actually killing the node. Indeed, it can be restarted by pressing `r`.

### robot_controller_node.py
This node controls the velocity of the robot wheels, by sending a constant angular twist of `1.0` around the z-axis. Consequently, the robot body rotates at a constant velocity.
Similarly to the camera node, we added multithreading in order to be able to stop the node by pressing `q` without actually killing the node. Indeed, it can be restarted by pressing `r`.

### gazebo_aruco.launch.py
We modified the launch file of the project in order to launch also the controller manager, needed later to correctly launch the `camera_controller_node.py`. For this, we added:
- `spawn_entity`
- `camera01_controller`

### robot4.xacro
We added a new link, called `arm_camera_link`, and its associated `arm_camera_joint` in order to add an arm where the camera could be position, so that it would be elevated from the robot body. For this, we changed the kinematic chain of the robot accordingly.

### config.yaml
We added the `joint_camera_controller` to the list of robot joints.

### setup.py
First of all, we needed to create a new package in Python, as the one provided had been created as a C++ package. As a consequence, it was not possible to efficiently add new nodes to the package and make them run in all computers (it worked only locally).

Then, we modified this file so that all the necessary files to correctly launch the project and make it work. Particularly, we imported the operating system, so that all the necessary paths to link the project folders could be defined relatively.

# Simulation: how to run
It is suggested to work with four terminals open.

First of all, the simulation must be started with the following command, in a terminal:
```
ros2 launch robot_urdf gazebo_aruco.launch.py
```
Then, there are two types of nodes that need to be launched:
- control nodes
- vision nodes

## Control nodes
There are two possibilities to make the robot move:
 1. Make the robot rotate
 2. Make the camera rotate

In the first case, the following command must be launched in a terminal:
```
ros2 run robot_urdf camera_controller_node
```
In the second case:
```
ros2 run robot_urdf robot_controller_node
```

In both cases, the robot can be stopped anytime by pressing `q`. The node will not be killed but just paused, so that it can be restarted by pressing `r`.
## Vision nodes
The vision nodes can be found in our [vision repo](https://github.com/annikadl/ros2_aruco.git).

For the vision part, two nodes need to be launched:
- `aruco_node`, part of the `ros2_aruco` package
- `vision_node`, the node we developed

Therefore, the following commands must be run in two different terminals:
```
ros2 run ros2_aruco aruco_node --ros-args --remap /image:=/robot/camera1/image_raw
```
and
```
ros2 run ros2_aruco vision_node
```

# Real robot: how to connect
For a full guide and troubleshooting, check the [Professor's repo](https://github.com/RICE-unige/rosbot_tutorials.git).

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
```
``` 
export ROS_IP=192.168.178.98
```
``` 
roslaunch tutorial_pkg all.launch
``` 

Done! Now this node will keep running all the drivers of the robot, so that it can be interfaced.

### Bridge terminal
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

### ROS2 interface terminal
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
