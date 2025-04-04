# Image args should come at the beginning.
ARG BASE_IMAGE

# hadolint ignore=DL3006
FROM $BASE_IMAGE as devel
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG ROS_DISTRO
ARG GITHUB_TOKEN
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
COPY ansible-galaxy-requirements.yaml /autoware/
COPY ansible/ /autoware/ansible/
WORKDIR /autoware
RUN ls /autoware

## Add GitHub to known hosts for private repositories
RUN mkdir -p ~/.ssh \
  && ssh-keyscan github.com >> ~/.ssh/known_hosts

## replace git@github with https://x-access-token
RUN sed -i "s/git@github\.com:/https:\/\/github\.com\//g" ./ansible-galaxy-requirements.yaml \
  && sed -i "s/https:\/\/github.com/https:\/\/x-access-token:$GITHUB_TOKEN@github.com/g" ./ansible-galaxy-requirements.yaml
## Set up development environment
RUN --mount=type=ssh ansible-galaxy collection install -f -r "ansible-galaxy-requirements.yaml"
RUN --mount=type=ssh ansible-playbook ansible/base_edge.yaml -e reload_system=no -e autoware_env_dir=/home/autoware \
  && pip uninstall -y ansible ansible-core

## Clean up unnecessary files
# hadolint ignore=DL3059
RUN rm -rf \
  "$HOME"/.cache \
  /etc/apt/sources.list.d/cuda*.list \
  /etc/apt/sources.list.d/docker.list \
  /etc/apt/sources.list.d/nvidia-docker.list \
  ~/.ros/ \
  ~/autoware_data/ \
  ~/.ssh/known_hosts \
  ~/.ansible \
  /autoware/

## Create entrypoint
# hadolint ignore=DL3059
RUN echo "source /opt/ros/${ROS_DISTRO}/install/setup.bash" > /etc/bash.bashrc
CMD ["/bin/bash"]
