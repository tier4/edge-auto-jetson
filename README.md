# edge-auto-jetson

This repository provides a sample ROS 2 environment working on a Jetson-based ECU and GMSL2-compatible cameras.

As a sample application, the following images show object detection results using the contents of this repository. Various perception applications will be added in
the future and you can develop them in this provided environment.

![object detection example](docs/sample.png "edge-auto-jetson object detection example")

## Prerequisites

### System Overview

This repository is based on a natively built ROS 2 environment. The system overview is shown below.

![system overview](docs/overview.drawio.svg "edge-auto-jetson overview")

### System Requirement

> [!NOTE]
> If you are using Jetson AGX Xavier based ECU, please refer to [this branch](https://github.com/tier4/edge-auto-jetson/tree/release/RQX-58G?tab=readme-ov-file).

- Camera: v4l2 compatible cameras, including [TIER IV Automotive HDR Camera C2](https://sensor.tier4.jp/automotive-hdr-camera)
- ECU: Jetson AGX Orin based ECU, including [ConnectTech Anvil](https://connecttech.com/product/anvil-embedded-system-with-nvidia-jetson-agx-orin/).
- NVIDIA L4T: R36.4 (including Ubuntu 22.04)
- ROS: ROS 2 Humble (native build)

## Getting Started

Please see [Tutorials](https://tier4.github.io/edge-auto-docs/getting_started/sensor_fusion_kit_v2_getting_started_guide.html).

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
  - ROS 2 package for unified ethernet-based LiDAR driver.
- [tier4/tier4_automotive_hdr_camera](https://github.com/tier4/tier4_automotive_hdr_camera)
  - Kernel driver for using TIER IV cameras with Video4Linux2 interface.
- [tier4/ros2_v4l2_camera](https://github.com/tier4/ros2_v4l2_camera)
  - ROS 2 package for camera driver using Video4Linux2.
- [tier4/sensor_trigger](https://github.com/tier4/sensor_trigger)
  - ROS 2 package for generating sensor trigger signals.
- [tier4/calibration_tools](https://github.com/tier4/CalibrationTools)
  - Repository for calibration tools to estimate parameters on autonomous driving systems.
- [autowarefoundation/autoware.universe](https://github.com/autowarefoundation/autoware.universe)
  - Repository for experimental, cutting-edge ROS packages for autonomous driving.
