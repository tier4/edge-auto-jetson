#!/bin/bash
colcon build \
    --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release \
    -DPython3_EXECUTABLE="$(which python3.10)" -DCMAKE_CUDA_STANDARD=14 \
    --packages-ignore cv_bridge \
    --allow-overriding image_geometry logging_demo \
    --packages-up-to edge_auto_jetson_launch
