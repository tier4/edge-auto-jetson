#!/bin/bash

SCRIPT_DIR=$(readlink -f "$(dirname "$0")")
ROOT_DIR=${SCRIPT_DIR}/..

echo "Docker build"
docker build --platform arm64 -t perception_ecu -f ${SCRIPT_DIR}/Dockerfile ${SCRIPT_DIR}

echo "Cloning all repositories under 'perception_ecu' directory"
mkdir -p ${ROOT_DIR}/src
vcs import ${ROOT_DIR}/src < ${ROOT_DIR}/perception_ecu.repos

echo "Building ROS packages in container"
${SCRIPT_DIR}/run.sh \
    "colcon build --symlink-install --packages-up-to perception_ecu_or_launch"
