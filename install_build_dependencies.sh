#!/bin/bash

sudo rosdep init
rosdep update
rosdep install -y \
    --from-paths $(colcon list --packages-up-to edge_auto_jetson_launch -p) \
    --ignore-src --skip-keys "autoware_launch libopencv-imgproc-dev"
