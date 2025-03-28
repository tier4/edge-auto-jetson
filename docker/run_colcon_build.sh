#!/bin/bash

SCRIPT_DIR=$(readlink -f "$(dirname "$0")")

echo "Building ROS packages in container"
"${SCRIPT_DIR}"/run.sh \
    "colcon build --symlink-install --cmake-force-configure --packages-up-to perception_ecu_launch --cmake-args -DCMAKE_POLICY_VERSION_MINIMUM=3.5"
