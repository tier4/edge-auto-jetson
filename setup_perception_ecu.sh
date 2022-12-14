#!/bin/bash
script_dir=$(cd $(dirname $0); pwd)

echo "Updating python and installing ansible modules"
sudo apt install -y python3.8
sudo apt install -y python3-pip
sudo python3.8 -m pip install --upgrade pip
sudo python3.8 -m pip install setuptools wheel
sudo python3.8 -m pip install --ignore-installed ansible

echo "Running ansible playbook to setup ECU"
ansible-playbook ${script_dir}/ansible/perception_ecu.yaml --ask-become-pass

echo "Cloning all repositories under 'perception_ecu' directory"
vcs import ${script_dir} < perception_ecu.repos

echo "Building ROS packages in container"
${script_dir}/perception_ecu/boot_env.sh \
             build_container \
             "colcon build --symlink-install --packages-up-to perception_ecu_or_launch"


