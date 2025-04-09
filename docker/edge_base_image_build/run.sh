#!/bin/bash -e
# cSpell: ignore persistents

eval ansible-playbook ansible/base_edge.yaml -e reload_system=no -e autoware_env_dir=/home/autoware
