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
You can stop whenever you want the 2 nodes pressing 'q'.


To launch the vision part you need ros2_aruco package.
Run the following commands:
```
ros2 run ros2_aruco aruco_node --ros-args --remap /image:=/robot/camera1/image_raw
```
and
```
ros2 run ros2_aruco vision_node
```

