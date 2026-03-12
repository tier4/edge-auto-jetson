# ros2_source_build

Builds [ROS 2](https://www.ros.org/) from source on Ubuntu 22.04 (e.g. Jetson), following the [Jazzy Ubuntu Development Setup](https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup.html).

## What it does

- Sets locale to UTF-8 (en_US.UTF-8)
- Enables Universe and ROS 2 apt sources (ros-apt-source)
- Installs development tools (ros-dev-tools, vcstool, colcon, pytest, etc.)
- Creates workspace at **`source_build_workspace_dir`** (default `~/source_builds_ws`), clones repos with `vcs import`, runs `rosdep install`
- Runs **`colcon build --install-base /opt/ros/{{ rosdistro }}`** so install layout matches the deb (no symlinks)
- Appends `source /opt/ros/{{ rosdistro }}/setup.bash` to `~/.bashrc`

**Cyclone DDS (rmw_cyclonedds_cpp)** is included in the official [ros2.repos](https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos).

## Variables

| Name                        | Required | Description                                                                 |
| --------------------------- | -------- | --------------------------------------------------------------------------- |
| rosdistro                   | no       | ROS distro (e.g. `jazzy`). Default: `jazzy`.                                |
| source_build_workspace_dir   | no       | Workspace path (src, build, log). Default: `~/source_builds_ws`.             |

- **Workspace** (src, build, log): **`source_build_workspace_dir`** — created under the connecting user's home; no root. You can delete this after a successful build to save space.
- **Install** (setup.bash, lib/, share/): **`/opt/ros/{{ rosdistro }}/`** — written by colcon with `--install-base` (same path as deb install).

## Example

```yaml
roles:
  - role: ros2_source_build
    vars:
      rosdistro: jazzy
      # source_build_workspace_dir: "{{ ansible_env.HOME }}/source_builds_ws"  # default
```

Defaults: `rosdistro` = `jazzy`, workspace = `~/source_builds_ws`, install = `/opt/ros/jazzy/`. Use `source /opt/ros/jazzy/setup.bash` as with the deb install.
