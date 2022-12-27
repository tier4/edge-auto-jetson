#!/bin/bash
SCRIPT_DIR=$(readlink -f "$(dirname "$0")")
ROOT_DIR=${SCRIPT_DIR}/..

COMMAND_IN_CONTAINER=${1:-/bin/bash}

source /opt/autoware/env/autoware.env

xhost +local:

docker run -it --rm --net host --privileged \
           --gpus all \
           -e CYCLONEDDS_URI \
           -e DISPLAY=$DISPLAY \
           -e RMW_IMPLEMENTATION \
           -e ROS_DOMAIN_ID \
           -v /opt/autoware:/opt/autoware \
           -v /sys:/sys \
           -v /tmp/.X11-unix/:/tmp/.X11-unix: \
           -v ${ROOT_DIR}:/workspace \
           -w /workspace \
           perception_ecu:latest \
           ${COMMAND_IN_CONTAINER}
