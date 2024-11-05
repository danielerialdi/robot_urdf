from setuptools import setup

package_name = 'robot_urdf'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='A package to control camera joint',
    license='TODO: License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_controller_node = robot_urdf.camera_controller_node:main',
        ],
    },
)
