#!/bin/bash
source /opt/autoware/env/autoware.env

SCRIPT_DIR=$(readlink -f "$(dirname "$0")")
ROOT_DIR=${SCRIPT_DIR}/..

COMMAND_IN_CONTAINER=${1:-/bin/bash}

docker run -it --rm --net host --privileged \
           --gpus all \
           -v /opt/autoware:/opt/autoware \
           -v /sys:/sys \
           -e CYCLONEDDS_URI \
           -e RMW_IMPLEMENTATION \
           -e ROS_DOMAIN_ID \
           -v ${ROOT_DIR}:/workspace \
           -w /workspace \
           perception_ecu:latest \
           ${COMMAND_IN_CONTAINER}
