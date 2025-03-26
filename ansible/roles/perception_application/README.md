# Perception Application Ansible Role

This Ansible role automates the installation and configuration of the Edge Auto Jetson perception application. It handles both the installation of the Edge Auto Jetson software and sets up an automatic startup service.

## Role Structure

```bash
perception_application/
├── tasks/
│   ├── main.yaml                    # Main task entry point
│   ├── build_edge_auto_jetson.yaml  # Edge Auto Jetson installation tasks
│   └── system_service.yaml          # Systemd service setup tasks
├── templates/
│   ├── run.sh.xx1_gen2.j2          # Template for XX1 Gen2 perception launch script
│   ├── run.sh.x2.j2                # Template for X2 perception launch script
│   └── perception-startup.service.j2 # Template for systemd service
├── defaults/
│   └── main.yaml                    # Default variable definitions
└── README.md                        # This documentation
```

## Role Variables

### Required Variables

- `perception_application_base_path`: Base installation path for the Edge Auto Jetson application
  - Example: `/home/autoware`
- `perception_application_edge_auto_version`: Git version/tag for Edge Auto Jetson repository
  - Example: `beta/v0.48`
- `perception_application_directory_name`: resulting directory of the cloned repository in the file system.
  - Example: `edge-auto-jetson` / `overlay_ws`
- `perception_application_edge_auto_repo`: Git repository URL for Edge Auto Jetson
  - Default: `git@github.com:tier4/edge-auto-jetson.xx1_gen2.0.git`
- `perception_application_native_built_ros`: Controls ROS build type
  - `true`: native built for Anvil Orin
  - `false`: apt install for X86 addons
- `perception_application_service_run_templates_file`: Template file for run script
  - Options: `run.sh.xx1_gen2.j2` or `run.sh.x2.j2`
- `perception_type`: Type of perception to run `tlr/od/addon`, will works as `jetson_{type}_launch` and `./build.sh {{ perception_type }}`

## Role Tasks

### 1. Edge Auto Jetson Installation

- Creates installation directory
- Clones Edge Auto Jetson repository
- Sets up build environment
- Configures ROS source paths based on architecture (X86/ARM)
- Builds the Edge Auto Jetson package

### 2. Automatic Launch System Service

- Creates service directory in `/opt/autoware/perception-startup-service`
- Installs launch script from appropriate template
- Configures and enables systemd service

## Dependencies

- ROS 2 Humble must be installed on the target system
- Git
- Python 3
- CUDA toolkit
- VCS tool

## Usage

Include this role in your playbook:

```yaml
- { role: perception_application, tags: [edge_auto_jetson_install] }
```

## Service Management

After installation, the perception service can be managed using standard systemd commands:

```bash
# Check service status
sudo systemctl status perception-startup.service

# Start the service
sudo systemctl start perception-startup.service

# Stop the service
sudo systemctl stop perception-startup.service

# Restart the service
sudo systemctl restart perception-startup.service
```

## Post-Installation

After successful installation:

1. The Edge Auto Jetson software will be installed in the specified base path
2. A systemd service will be configured to automatically start the perception application
3. The service will be enabled to start on boot

## Troubleshooting

1. If the build fails:
   - Check ROS 2 Humble installation
   - Verify CUDA toolkit installation
   - Check network connectivity for git clone
   - Review build logs in the installation directory

2. If the service fails to start:
   - Check service logs: `journalctl -u perception-startup.service`
   - Verify file permissions in the installation directory
   - Ensure all ROS 2 dependencies are properly sourced