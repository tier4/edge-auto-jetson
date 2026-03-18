# ros2_source_build

Builds [ROS 2](https://www.ros.org/) from source on Ubuntu 22.04 (e.g. Jetson), following the [Jazzy Ubuntu Development Setup](https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup.html).

## What it does

- Sets locale to UTF-8 (en_US.UTF-8)
- Enables Universe and installs [ros-apt-source](https://github.com/ros-infrastructure/ros-apt-source) (latest release from GitHub) for ROS 2 apt keys and source list
- Installs development tools: `python3-rosinstall-generator`, `ros-dev-tools`, flake8, pytest, mypy, etc.
- Creates workspace at **`source_build_workspace_dir`** (default `~/source_builds_ws`) with a `src` directory
- **ROS 2 base**: runs `rosinstall_generator --deps --rosdistro <ros_distro> <ros_variant>` and pipes the result to `vcs import`. The package set is defined by **`ros_variant`** ([REP-2001](https://www.ros.org/reps/rep-2001.html), e.g. `ros_base`)
- **Extra packages**: when any of `extra_rosinstall_packages`, `extra_system_packages`, or `extra_python_packages` is non-empty, runs `extra_packages.yaml`, which:
  - Installs `extra_system_packages` (apt) and `extra_python_packages` (pip)
  - If `extra_rosinstall_packages` is non-empty: generates `ros2.<ros_distro>.extra.rosinstall` with `rosinstall_generator --deps`, then runs `vcs import --skip-existing` for those packages
- Runs `rosdep init` (if not already done), `rosdep update`, then `rosdep install --from-paths src --ignore-src` with `--skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"`
- Runs **`colcon build --merge-install --install-base /opt/ros/{{ ros_distro }}`** with `-DCMAKE_BUILD_TYPE=Release` (install layout matches the deb)
- Appends `source /opt/ros/{{ ros_distro }}/setup.bash` to `~/.bashrc`

## Variables

| Name                       | Required | Description |
| -------------------------- | -------- | ----------- |
| ros_distro                  | no       | ROS distro (e.g. `jazzy`). Default: `jazzy`. |
| ros_variant                | no       | REP-2001 variant for the base source set (e.g. `ros_base`, `ros_core`). Default: `ros_base`. |
| source_build_workspace_dir | no       | Workspace path (src, build, log). Default: `~/source_builds_ws`. |
| extra_rosinstall_packages | no       | Extra ROS package names for `rosinstall_generator`. Package names like `cv_bridge`, not apt names like `ros-jazzy-cv-bridge`. If empty, the extra rosinstall/vcs step is skipped. |
| extra_system_packages     | no       | Extra apt packages (e.g. libs, dev tools). Defaults include build tools and other deps for the default extra ROS packages (e.g. geographic, grid_map, perception_pcl). |
| extra_python_packages     | no       | Extra pip packages. Defaults include empy, pytest, flake8 plugins, etc. |

- **Workspace** (src, build, log): **`source_build_workspace_dir`** — created under the connecting user's home; no root. You can delete it after a successful build to save space.
- **Install** (setup.bash, lib/, share/): **`/opt/ros/{{ ros_distro }}/`** — written by colcon with `--install-base` (same path as deb install).
- **Extra source**: generated as `ros2.<ros_distro>.extra.rosinstall` inside the workspace and imported with `vcs import --skip-existing`.

## Example

```yaml
roles:
  - role: ros2_source_build
    vars:
      ros_distro: jazzy
      # ros_variant: ros_base   # default
      # source_build_workspace_dir: "{{ ansible_env.HOME }}/source_builds_ws"  # default
      # extra_rosinstall_packages:
      #   - cv_bridge
      #   - v4l2_camera
      # extra_system_packages:
      #   - libopencv-dev
      # extra_python_packages:
      #   - pytest
```

Defaults: `ros_distro` = `jazzy`, `ros_variant` = `ros_base`, workspace = `~/source_builds_ws`, install = `/opt/ros/jazzy/`. Use `source /opt/ros/jazzy/setup.bash` as with the deb install.
