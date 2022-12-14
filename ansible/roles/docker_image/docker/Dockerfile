ARG OVERLAY_WS=/workspace
ARG L4T_RELEASE=32
ARG L4T_REVISION_MAJOR=6
ARG L4T_REVISION_MINOR=1
ARG L4T_VERSION=$L4T_RELEASE.$L4T_REVISION_MAJOR.$L4T_REVISION_MINOR

FROM dustynv/ros:galactic-ros-base-l4t-r$L4T_VERSION

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libogg-dev \
        libvorbis-dev \
        libtheora-dev \
        gcc-8 \
        g++-8 \
    && rm -rf /var/lib/apt/list/*

# Update gcc / g++ to compile recent autoware
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 100 \
    --slave /usr/bin/g++ g++ /usr/bin/g++-8

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
WORKDIR /
