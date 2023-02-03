ARG L4T_RELEASE=32
ARG L4T_REVISION_MAJOR=6
ARG L4T_REVISION_MINOR=1
ARG L4T_VERSION=$L4T_RELEASE.$L4T_REVISION_MAJOR.$L4T_REVISION_MINOR

FROM dustynv/ros:galactic-ros-base-l4t-r$L4T_VERSION

# Fix GPG key to support recent key update
RUN wget -q -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null \
    && echo 'deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ bionic main' | tee /etc/apt/sources.list.d/kitware.list >/dev/null \
    && sed -i 's|deb https://apt.kitware.com/ubuntu/ bionic main|#&|g' /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    g++-8 \
    gcc-8 \
    libogg-dev \
    libqt5qml5 \
    libtheora-dev \
    libvorbis-dev \
    python3-matplotlib \
    python3-numpy \
    python3-ruamel.yaml \
    python3-tk \
    && rm -rf /var/lib/apt/list/*

# Update gcc / g++ to compile recent autoware
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 100 \
    --slave /usr/bin/g++ g++ /usr/bin/g++-8

# Install PySide2 to use GUI applications
RUN wget --progress=dot:giga \
    https://github.com/hiroyuki-s1/PySide2InstallForJetson/raw/main/dist/PySide2-5.9.0a1-5.9.5-cp36-cp36m-linux_aarch64.whl \
    && pip3 install --user --no-cache-dir PySide2-5.9.0a1-5.9.5-cp36-cp36m-linux_aarch64.whl

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
WORKDIR /
