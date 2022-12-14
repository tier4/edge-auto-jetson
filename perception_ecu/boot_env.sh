#!/bin/bash
source /opt/autoware/env/autoware.env

script_dir=$(cd $(dirname $0); pwd)
container_name=${1:-perception_ecu}
command_in_container=${2:-/bin/bash}

docker run -it --rm --name ${container_name} --net host --privileged \
       --gpus all \
       -v /opt/autoware:/opt/autoware \
       -v /sys:/sys \
       -e CYCLONEDDS_URI \
       -e RMW_IMPLEMENTATION \
       -e ROS_DOMAIN_ID \
       -v ${script_dir}/workspace:/workspace \
       -w /workspace \
       perception_ecu:latest \
       ${command_in_container}
