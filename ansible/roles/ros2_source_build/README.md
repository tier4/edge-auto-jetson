# ros2_source_build

This role builds [ROS 2](https://www.ros.org/) from source, following the [Jazzy Ubuntu Development Setup](https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup.html). Intended for Ubuntu 22.04 (e.g. Jetson) where a binary distribution may not be available or you need a source install.

It will:

- Set locale to UTF-8 (en_US.UTF-8)
- Enable Universe and ROS 2 apt sources (ros-apt-source)
- Install development tools (ros-dev-tools, vcstool, colcon, pytest, etc.)
- Clone the ROS 2 repos via `vcs import` and run `rosdep install`
- Run `colcon build --symlink-install` in the workspace (e.g. `~/ros2_jazzy`)
- Copy the `install` tree to **`/opt/ros/{{ rosdistro }}/`** (dereferencing symlinks) so the same path as deb install works
- Add `source /opt/ros/{{ rosdistro }}/setup.bash` to `~/.bashrc`

You can use `source /opt/ros/<distro>/setup.bash` (e.g. `/opt/ros/jazzy/setup.bash`) as with the standard deb-based install.

**Cyclone DDS (rmw_cyclonedds_cpp)** is already included in the official [ros2.repos](https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos) (`eclipse-cyclonedds/cyclonedds` and `ros2/rmw_cyclonedds`).

## Inputs

| Name              | Required | Description                                              |
| ----------------- | -------- | -------------------------------------------------------- |
| rosdistro         | false    | ROS distro to build (e.g. `jazzy`). Default: `jazzy`.    |
| source_workspace  | false    | Workspace path (e.g. `~/ros2_jazzy`). Default: `~/ros2_{{ rosdistro }}`. |

## Example

```yaml
roles:
  - role: ros2_source_build
    vars:
      rosdistro: jazzy
      # source_workspace: "~/ros2_jazzy"  # optional
```

For a Jetson playbook that uses Jazzy from source instead of the `ros2` (deb) role:

```yaml
roles:
  - role: ros2_source_build
```

Default `rosdistro` is `jazzy`; the workspace is built at `~/ros2_jazzy` and the result is installed to `/opt/ros/jazzy/` so that `source /opt/ros/jazzy/setup.bash` works like the deb install.
