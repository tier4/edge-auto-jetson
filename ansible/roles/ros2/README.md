# ROS2

This role installs [ROS 2](https://docs.ros.org) under `/opt/ros`. Because apt binaries for the latest ROS 2 distribution are not available on some NVIDIA L4T environments, such as L4T R32.6.1 (based on Ubuntu18.04), this role installs dependencies, clones ROS 2 source codes, and builds them.

## Inputs
| Name       | Required | Description                                                  |
| ros_distro | true     | The ROS distribution. Currently, only `humble` is supported. |

