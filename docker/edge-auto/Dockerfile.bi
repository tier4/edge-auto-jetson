# Image args should come at the beginning.
ARG BASE_IMAGE

# hadolint ignore=DL3006
FROM $BASE_IMAGE as devel
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG ROS_DISTRO
ARG DESCRIPTION

LABEL org.opencontainers.image.description=$DESCRIPTION

## Install apt packages
# hadolint ignore=DL3008
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
  git \
  ssh \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

## Copy files
COPY .ansible-galaxy-requirements.yaml /autoware/
COPY ansible/ /autoware/ansible/
WORKDIR /autoware
RUN ls /autoware

## Add GitHub to known hosts for private repositories
RUN mkdir -p ~/.ssh \
  && ssh-keyscan github.com >> ~/.ssh/known_hosts

## Set up development environment
RUN --mount=type=ssh ansible-playbook ansible/base_edge.yaml -e reload_system=no -e autoware_env_dir=/home/autoware \
  -e ros_distro=${ROS_DISTRO}

## Clean up unnecessary files
# hadolint ignore=DL3059
RUN rm -rf \
  "$HOME"/.cache \
  ~/.ros/ \
  ~/autoware_data/ \
  ~/.ssh/known_hosts \
  ~/.ansible \
  /autoware/

## Create entrypoint
# hadolint ignore=DL3059
CMD ["/bin/bash"]
