#!/bin/bash
SCRIPT_DIR=$(readlink -f "$(dirname "$0")")
ROOT_DIR="${SCRIPT_DIR}"/..

COMMAND_IN_CONTAINER="${1:-/bin/bash}"

# shellcheck disable=SC1091
source /opt/autoware/env/autoware.env

docker run -it --rm --net host --privileged \
    --gpus all \
    -e CYCLONEDDS_URI \
    -e DISPLAY="${DISPLAY}" \
    -e NO_AT_BRIDGE=1 \
    -e RMW_IMPLEMENTATION \
    -e ROS_DOMAIN_ID \
    -v "${HOME}"/.Xauthority:/root/.Xauthority:rw \
    -v "${ROOT_DIR}":/workspace \
    -v /opt/autoware:/opt/autoware \
    -v /sys:/sys \
    -v /tmp/.X11-unix/:/tmp/.X11-unix: \
    -w /workspace \
    perception_ecu:latest \
    /bin/bash -c "${COMMAND_IN_CONTAINER}"
