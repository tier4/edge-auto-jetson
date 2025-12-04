# ROS 2

This role installs [ROS 2](http://www.ros2.org/) on Ubuntu systems following the [official installation guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html), with additional development dependencies and tools.

## Overview

This role performs a complete ROS 2 installation including:

- Setting up ROS 2 repositories and GPG keys
- Installing core ROS 2 packages based on the specified distribution
- Installing development dependencies and tools
- Configuring environment setup
- Initializing and updating rosdep

## Inputs

| Name              | Required | Description                                                 |
| ----------------- | -------- | ----------------------------------------------------------- |
| ros_distro        | true     | The ROS 2 distribution to install (e.g., humble, iron)      |
| installation_type | false    | Installation type: `desktop` (full) or `ros-base` (minimal) |

## Default Configuration

The default `installation_type` can be found in:
[./defaults/main.yaml](./defaults/main.yaml)

## Features

This role:

- Authorizes the ROS GPG key
- Configures the appropriate ROS 2 apt repository
- Installs basic system dependencies
- Installs comprehensive ROS 2 development dependencies
- Installs Python dependencies with specific versions where required
- Installs Python code quality tools
- Installs the specified ROS 2 distribution
- Installs additional ROS 2 packages and tools for development
- Configures environment setup in .bashrc
- Initializes and updates rosdep

## Additional Packages

The role installs numerous additional ROS 2 packages beyond the base installation, including:

- Launch tools (XML, YAML, testing)
- Demo nodes
- Computer vision packages
- PCL (Point Cloud Library) integration
- Diagnostic tools
- Navigation packages
- Testing frameworks
- And many more development utilities

This comprehensive setup provides everything needed for ROS 2 development, including tools for visualization, simulation, and testing.
