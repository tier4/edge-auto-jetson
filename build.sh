#!/bin/bash
colcon build \
       --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release \
       -DPython3_EXECUTABLE=$(which python3.6) -DCMAKE_CUDA_STANDARD=14 \
       --packages-up-to edge_auto_jetson_launch
