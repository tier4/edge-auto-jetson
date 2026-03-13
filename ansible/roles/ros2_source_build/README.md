# ros2_source_build

Builds [ROS 2](https://www.ros.org/) from source on Ubuntu 22.04 (e.g. Jetson), following the [Jazzy Ubuntu Development Setup](https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup.html).

## What it does

- Sets locale to UTF-8 (en_US.UTF-8)
- Enables Universe and ROS 2 apt sources (ros-apt-source)
- Installs development tools (ros-dev-tools, vcstool, colcon, pytest, etc.)
- Creates workspace at **`source_build_workspace_dir`** (default `~/source_builds_ws`), imports the core ROS 2 sources with `vcs import`
- When `extra_system_packages` or `extra_rosinstall_packages` is non-empty, installs `python3-rosinstall-generator` and any packages listed in `extra_system_packages`
- When `extra_rosinstall_packages` is non-empty, generates a `.rosinstall` file with `rosinstall_generator`, and imports only the selected extra packages and their dependencies with `vcs import --skip-existing`
- Runs `rosdep install`
- Runs **`colcon build --install-base /opt/ros/{{ rosdistro }}`** so install layout matches the deb (no symlinks)
- Appends `source /opt/ros/{{ rosdistro }}/setup.bash` to `~/.bashrc`

**Cyclone DDS (rmw_cyclonedds_cpp)** is included in the official [ros2.repos](https://raw.githubusercontent.com/ros2/ros2/jazzy/ros2.repos).

## Variables

| Name                       | Required | Description |
| -------------------------- | -------- | ----------- |
| rosdistro                  | no       | ROS distro (e.g. `jazzy`). Default: `jazzy`. |
| source_build_workspace_dir | no       | Workspace path (src, build, log). Default: `~/source_builds_ws`. |
| extra_rosinstall_packages  | no       | Extra ROS package names passed to `rosinstall_generator`. These are package names such as `cv_bridge`, not apt package names such as `ros-jazzy-cv-bridge`. If empty, the extra import step is skipped. |
| extra_system_packages      | no       | Extra apt packages to install in addition to the base development tools. Defaults include OpenCV/PCL-related libraries and other package-specific dependencies. |
| extra_rosinstall_file      | no       | Output path of the generated `.rosinstall` file. |

- **Workspace** (src, build, log): **`source_build_workspace_dir`** — created under the connecting user's home; no root. You can delete this after a successful build to save space.
- **Install** (setup.bash, lib/, share/): **`/opt/ros/{{ rosdistro }}/`** — written by colcon with `--install-base` (same path as deb install).
- **Extra source import**: generated from `extra_rosinstall_packages` via `rosinstall_generator`. `jazzy_extra.repos` is not used by the current implementation.

## Example

```yaml
roles:
  - role: ros2_source_build
    vars:
      rosdistro: jazzy
      # source_build_workspace_dir: "{{ ansible_env.HOME }}/source_builds_ws"  # default
      # extra_rosinstall_packages:
      #   - cv_bridge
      #   - v4l2_camera
      # extra_system_packages:
      #   - libopencv-dev
      #   - libpcl-dev
```

Defaults: `rosdistro` = `jazzy`, workspace = `~/source_builds_ws`, install = `/opt/ros/jazzy/`. Use `source /opt/ros/jazzy/setup.bash` as with the deb install. `extra_system_packages` and `extra_rosinstall_packages` are independent controls, and neither depends on a hard-coded distro check.
