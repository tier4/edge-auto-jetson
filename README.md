# edge-auto-jetson

This repository provides a sample ROS2 environment working on a Jetson-based ECU and GMSL2-compatible cameras.

As a sample application, the following images show object recognition results using the contents of this repository. Various perception applications will be added in 
the future and you can develop them in this provided environment.

[Edge.Auto](http://edge.auto) sensor fusion system can be realized by using this with [edge-auto](https://github.com/tier4/edge-auto) repository.

![object recognition example](docs/sample.png "edge-auto-jetson object recognition example")

# Prerequisites

### System Overview

This repository is based on a natively built ROS2 environment. The system overview is shown below.

![system overview](docs/overview.drawio.svg "edge-auto-jetson overview")

### System Requirement

- Camera: v4l2 compatible cameras, including [TIER IV Automotive HDR Camera C1](https://sensor.tier4.jp/automotive-hdr-camera)
- ECU: Jetson AGX Xavier based ECU, including [RQX-58G](https://www.adlinktech.com/Products/ROS2_Solution/ROS2_Controller/RQX-580_58G) from ADLINK Technology Inc. and [Developer Kit](https://www.nvidia.com/ja-jp/autonomous-machines/embedded-systems/jetson-agx-xavier) from NVIDIA Corp.
- NVIDIA L4T: R32.6.1 (including Ubuntu 18.04)
- ROS: ROS2 Humble (native build)

## Getting Started

Please see [Tutorials](https://github.com/tier4/edge-auto/tree/main/docs/tutorials.md).

## Related repositories

- [tier4/edge-auto](https://github.com/tier4/edge-auto)
  - Meta-repository containing `autoware.repos` to construct ROS-based workspace on x86-based ECU.
- [tier4/edge-auto-jetson](https://github.com/tier4/edge-auto-jetson)
  - Meta-repository containing `autoware.repos` file to construct ROS-based workspace on Jetson-based ECU.
- [tier4/edge_auto_launch](https://github.com/tier4/edge_auto_launch)
  - Launch configuration repository containing node configurations and their parameters for x86-based ECU.
- [tier4/edge_auto_jetson_launch](https://github.com/tier4/edge_auto_jetson_launch)
  - Launch configuration repository containing node configurations and their parameters for Jetson-based ECU.
- [tier4/edge_auto_individual_params](https://github.com/tier4/edge_auto_individual_params)
  - Repository for managing system parameters including camera parameters, driver parameters, etc.
- [tier4/nebula](https://github.com/tier4/nebula)
  - ROS2 package for unified ethernet-based LiDAR driver.
- [tier4/ros2_v4l2_camera](https://github.com/tier4/ros2_v4l2_camera)
  - ROS2 package for camera driver using Video4Linux2.
- [tier4/sensor_trigger](https://github.com/tier4/sensor_trigger)
  - ROS2 package for generating sensor trigger signals.
- [tier4/calibration_tools](https://github.com/tier4/CalibrationTools)
  - Repository for calibration tools to estimate parameters on autonomous driving systems.
- [autowarefoundation/autoware.universe](https://github.com/autowarefoundation/autoware.universe)
  - Repository for experimental, cutting-edge ROS packages for autonomous driving.
