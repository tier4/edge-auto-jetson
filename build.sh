#!/bin/bash

sudo jetson_clocks
export MAKEFLAGS="-j8"

colcon build \
    --symlink-install \
    --cmake-args \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_CUDA_STANDARD=14 \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--no-as-needed -lgmp -lmpfr" \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--no-as-needed -lgmp -lmpfr" \
    -DPython3_EXECUTABLE="$(which python3.10)" \
    --allow-overriding image_geometry logging_demo cv_bridge \
    --packages-up-to edge_auto_jetson_launch
