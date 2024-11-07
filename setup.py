from setuptools import setup
from glob       import glob
import os

package_name = 'robot_urdf'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        (os.path.join('share', package_name, 'urdf'), glob('gazebo/*.gazebo')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='daniele.rialdi@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
<<<<<<< HEAD
            'camera_controller_node = robot_urdf.camera_controller_node:main'
=======
        	'camera_controller_node = robot_urdf.camera_controller_node:main',
        	'robot_controller_node = robot_urdf.robot_controller_node:main',
>>>>>>> c08063b9da5f75c2425b64a1f5d82e4b9b2a76d7
        ],
    },
)
