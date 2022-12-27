#!/bin/bash

SCRIPT_DIR=$(readlink -f "$(dirname "$0")")

echo -e "\e[36mUpdating python and installing ansible modules.\e[0m"

# Install sudo
if ! (command -v sudo >/dev/null 2>&1); then
    apt-get -y update
    apt-get -y install sudo
fi

# Install git
if ! (command -v git >/dev/null 2>&1); then
    sudo apt-get -y update
    sudo apt-get -y install git
fi

# Install python3.8 for ansible
if ! (command -v python3.8 >/dev/null 2>&1); then
    sudo apt-get -y update
    sudo apt-get -y install python3.8
fi

# Install pip for ansible
if ! (command -v pip3 >/dev/null 2>&1); then
    sudo apt-get -y update
    sudo apt-get -y install python3-pip
    python3.8 -m pip install --upgrade pip
fi

# Install ansible
ansible_version=$(python3.8 -m pip list | grep -oP "^ansible\s+\K([0-9]+)" || true)
if [ "$ansible_version" != "6" ]; then
    sudo apt-get -y purge ansible
    python3.8 -m pip install setuptools wheel
    python3.8 -m pip install --upgrade "ansible==6.*"
fi

# For Python packages installed with user privileges
export PATH="$HOME/.local/bin:$PATH"

echo "Running ansible playbook to setup ECU"

# Run ansible
if ansible-playbook ${SCRIPT_DIR}/ansible/setup.yaml --ask-become-pass; then
    echo -e "\e[32mCompleted.\e[0m"
    exit 0
else
    echo -e "\e[31mFailed.\e[0m"
    exit 1
fi
