# edge-auto-jetson

This repository provides a sample ROS2 environment working on a Jetson AGX Xavier based ECU and GMSL2-compatible cameras.

As a sample application, the following images show object recognition results using the contents of this repository. Various perception applications will be added in the future and you can develop them in this provided environment.

![object recognition example](docs/sample.png "perception_ecu_container object recognition example")

## Prerequisites

### System Overview

This repository is based on a natively built ROS2 environment. The system overview is shown below.

![system overview](docs/overview.drawio.svg "perception_ecu_container overview")

### System Requirement

- Camera: v4l2 compatible cameras, including [TIER IV Automotive HDR Camera C1](https://sensor.tier4.jp/automotive-hdr-camera)
- ECU: Jetson AGX Xavier based ECU, including [RQX-58G](https://www.adlinktech.com/Products/ROS2_Solution/ROS2_Controller/RQX-580_58G) from ADLINK Technology Inc. and [Developer Kit](https://www.nvidia.com/ja-jp/autonomous-machines/embedded-systems/jetson-agx-xavier) from NVIDIA Corp.
- Board support packages: NVIDIA L4T R32.6.1 (including Ubuntu 18.04) or higher

## Getting Started

Please see [Tutorials](https://github.com/tier4/edge-auto/tree/main/docs/tutorials.md).

## Related repositories

- [tier4/perception_ecu_container](https://github.com/tier4/perception_ecu_container)
  - Meta-repository containing `.repos` file to construct ROS-based workspace on Jetson.
- [tier4/perception_ecu_launch](https://github.com/tier4/perception_ecu_launch.git)
  - Launch configuration repository containing node configurations and their parameters for Perception ECU.
- [tier4/perception_ecu_individual_params](https://github.com/tier4/perception_ecu_individual_params)
  - Repository for managing Perception ECU parameters including camera parameters, driver parameters, etc.
- [tier4/sensor_trigger](https://github.com/tier4/sensor_trigger.git)
  - ROS2 package for generating sensor trigger signals.
- [tier4/ros2_v4l2_camera](https://github.com/tier4/ros2_v4l2_camera.git)
  - ROS2 camera driver using Video4Linux2.
- [autowarefoundation/autoware.universe](https://github.com/autowarefoundation/autoware.universe.git)
  - Repository for experimental, cutting-edge ROS packages for Autonomous Driving.
- [tier4/edge-auto](https://github.com/tier4/edge-auto.git)
  - Meta-repository containing `.repos` to construct ROS-based workspace on x86 (i.e., Host) PC.
