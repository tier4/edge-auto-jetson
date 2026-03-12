# ros2_source_build

This role builds [ROS 2](https://www.ros.org/) from source, following the [Jazzy Ubuntu Development Setup](https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup.html).

It will:

- Set locale to UTF-8 (en_US.UTF-8)
- Enable Universe and ROS 2 apt sources (ros-apt-source)
- Install development tools (ros-dev-tools, vcstool, colcon, pytest, etc.)
- Clone the ROS 2 repos via `vcs import` and run `rosdep install`
- Clone repos with `vcs import` into **`/opt/ros/{{ rosdistro }}/src`**, run rosdep and **`colcon build`** with `--install-base /opt/ros/{{ rosdistro }}` (src, build, install all under `/opt/ros/<distro>/`)
- Add `source /opt/ros/{{ rosdistro }}/setup.bash` to `~/.bashrc`

You can use `source /opt/ros/<distro>/setup.bash` (e.g. `/opt/ros/jazzy/setup.bash`) as with the standard deb-based install.

**Cyclone DDS (rmw_cyclonedds_cpp)** is already included in the official [ros2.repos](https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos) (`eclipse-cyclonedds/cyclonedds` and `ros2/rmw_cyclonedds`).

## Inputs

| Name              | Required | Description                                              |
| ----------------- | -------- | -------------------------------------------------------- |
| rosdistro         | false    | ROS distro to build (e.g. `jazzy`). Default: `jazzy`.     |

The workspace (src, build, install) is under **`/opt/ros/{{ rosdistro }}/`**.


## Example (in your playbook)

```yaml
roles:
  - role: ros2_source_build
    vars:
      rosdistro: jazzy
```

Default `rosdistro` is `jazzy`; src, build, and install all live under `/opt/ros/jazzy/`, and `source /opt/ros/jazzy/setup.bash` works like the deb install.
