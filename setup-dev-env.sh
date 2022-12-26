#!/bin/bash

SCRIPT_DIR=$(readlink -f "$(dirname "$0")")

echo "\e[36mUpdating python and installing ansible modules\e[m"

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

# Install pipx for ansible
if ! (python3 -m pipx --version >/dev/null 2>&1); then
    sudo apt-get -y update
    sudo apt-get -y install python3-pip python3-venv
    python3 -m pip install --user pipx
fi

# Install ansible
python3 -m pipx ensurepath
export PATH="${PIPX_BIN_DIR:=$HOME/.local/bin}:$PATH"
pipx install --include-deps --force "ansible==6.*"

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
