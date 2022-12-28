#!/bin/bash

SCRIPT_DIR=$(readlink -f "$(dirname "$0")")

echo "Building docker image based on Dockerfile"
docker build --platform arm64 -t perception_ecu -f "${SCRIPT_DIR}"/Dockerfile "${SCRIPT_DIR}"
