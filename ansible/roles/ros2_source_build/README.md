# ros2_source_build

This role builds [ROS 2](https://www.ros.org/) from source, following the [Jazzy Ubuntu Development Setup](https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup.html).

It will:

- Set locale to UTF-8 (en_US.UTF-8)
- Enable Universe and ROS 2 apt sources (ros-apt-source)
- Install development tools (ros-dev-tools, vcstool, colcon, pytest, etc.)
- Clone the ROS 2 repos via `vcs import` and run `rosdep install`
- Clone repos with `vcs import` into **`/opt/ros/{{ rosdistro }}/src`**, run rosdep and **`colcon build`** (no `--install-base`; install goes to `.../install/`)
- Add `source /opt/ros/{{ rosdistro }}/install/setup.bash` to `~/.bashrc`

Use `source /opt/ros/<distro>/install/setup.bash` (path differs from deb install, which uses `.../setup.bash`).

**Cyclone DDS (rmw_cyclonedds_cpp)** is already included in the official [ros2.repos](https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos) (`eclipse-cyclonedds/cyclonedds` and `ros2/rmw_cyclonedds`).

## Inputs

| Name              | Required | Description                                              |
| ----------------- | -------- | -------------------------------------------------------- |
| rosdistro         | false    | ROS distro to build (e.g. `jazzy`). Default: `jazzy`.     |

- **Workspace** (src, build, install/): **`/opt/ros/{{ rosdistro }}/`**. No `--install-base` so colcon writes to `install/` and does not put `COLCON_IGNORE` in the root.


## Example (in your playbook)

```yaml
roles:
  - role: ros2_source_build
    vars:
      rosdistro: jazzy
```

Default `rosdistro` is `jazzy`; workspace is `/opt/ros/jazzy/` (src, build, install/). Source with `source /opt/ros/jazzy/install/setup.bash`.
