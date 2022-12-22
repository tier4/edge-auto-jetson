ARG OVERLAY_WS=/opt/ros/overlay_ws
ARG L4T_RELEASE=32
ARG L4T_REVISION_MAJOR=6
ARG L4T_REVISION_MINOR=1
ARG L4T_VERSION=$L4T_RELEASE.$L4T_REVISION_MAJOR.$L4T_REVISION_MINOR

FROM dustynv/ros:galactic-ros-base-l4t-r$L4T_VERSION AS base

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gstreamer1.0-tools gstreamer1.0-alsa \
        gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
        gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
        gstreamer1.0-libav \
        libgstreamer1.0-dev \
        libgstreamer-plugins-base1.0-dev \
        libgstreamer-plugins-good1.0-dev \
        libogg-dev \
        libvorbis-dev \
        libtheora-dev \
    && rm -rf /var/lib/apt/list/*


FROM base AS builder

ARG OVERLAY_WS
WORKDIR $OVERLAY_WS/src

COPY ./docker/overlay.repos ../
RUN vcs import ./ < ../overlay.repos

# build overlay source
WORKDIR $OVERLAY_WS

RUN . /opt/ros/"$ROS_DISTRO"/install/setup.sh && \
    colcon build \
      --cmake-args -DCMAKE_BUILD_TYPE=Release \
      --merge-install \
      --packages-up-to gscam jetson_camera_trigger image_pipeline image_transport_plugins\
      --event-handlers console_cohesion+


FROM base AS jetson_camera

ARG OVERLAY_WS
COPY --from=builder ${OVERLAY_WS}/install ${OVERLAY_WS}/install
COPY --from=builder ${OVERLAY_WS}/src ${OVERLAY_WS}/src
ENV OVERLAY_WS=${OVERLAY_WS}

# source entrypoint setup
RUN sed --in-place --expression \
      '$isource "$OVERLAY_WS/install/setup.bash"' \
      /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
WORKDIR /
