#!/bin/bash
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

perception_type=$1
if [ -z "$perception_type" ]; then
    echo "Usage: $0 <perception_type>"
    exit 1
fi


if [ "$perception_type" = "addon" ]; then
    echo "Running rosdep update and install for addon..."
    rosdep update
    rosdep install --from-paths src --ignore-src -r -y
fi

colcon build \
    --symlink-install --cmake-force-configure \
    --packages-up-to edge_auto_jetson_launch \
    --cmake-args -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-w" -DCMAKE_CUDA_STANDARD=14 -DCMAKE_CUDA_ARCHITECTURES=87 -DCMAKE_CUDA_COMPILER=/usr/local/cuda/bin/nvcc -DBUILD_TESTING=OFF \
    -DPython3_EXECUTABLE="$(which python3)" \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5
