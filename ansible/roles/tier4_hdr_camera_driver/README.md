# TIER4 HDR Camera Driver (GMSL)

This Ansible role installs the TIER4 HDR Camera GMSL driver on ARM64 systems. The role handles downloading the driver package from a GitHub repository, preparing the system for installation, and setting up a service to complete the installation at boot time.

## Overview

The TIER4 HDR Camera Driver provides support for GMSL (Gigabit Multimedia Serial Link) cameras, commonly used in autonomous driving and robotics applications. This role automates the installation process, which requires special handling due to kernel module dependencies.

## Requirements

- Ubuntu operating system (ARM64 architecture)
- Ansible 2.9 or higher
- Internet access to download the driver package from GitHub

## Role Variables

| Name                       | Required | Description                                                                                                                  |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| camera_driver_repo         | yes      | URL to the GitHub API endpoint for the release assets                                                                        |
| camera_driver_download_dir | yes      | Local directory where the driver package will be downloaded                                                                  |
| exposure_time              | no       | Exposure length in microseconds to be set in the driver configuration file (default: `11000`)                                |
| distortion_correction      | no       | Enable/disable the distortion correction function supported by the camera hardware (`1`: Enable, `0`: Disable. default: `0`) |

## Installation Process

This role performs the following steps:

1. Fetches information about the camera driver release from GitHub
2. Parses the download URL for the appropriate ARM64 driver package
3. Downloads the driver package from the repository
4. Installs required build dependencies (make, build-essential, dkms, etc.)
5. Unpacks the driver package without triggering post-installation scripts
6. Marks the package as "hold" to prevent automatic updates
7. Creates a custom installer script to complete the installation at boot time
8. Sets up a systemd service to run the installer script on system startup

## Boot-time Installation

The driver installation is completed at boot time because:

- Kernel module compilation needs to match the running kernel
- This approach ensures the driver is properly rebuilt after kernel updates
- It prevents installation failures during the Ansible deployment phase

## Usage

Include this role in your playbook:

```yaml
- hosts: camera_systems
  roles:
    - tier4_hdr_camera_driver
```

## Notes

- The driver package is specifically for ARM64 architecture
- The role searches for packages matching the pattern `tier4-camera-gmsl_(.+)_arm64.deb`
- The installation process uses DKMS (Dynamic Kernel Module Support) to build the driver for the current kernel

## Troubleshooting

If the camera driver fails to load after installation:

1. Check the systemd service status:

   ```
   sudo systemctl status camera-driver-installer
   ```

2. Review the installation logs:

   ```
   sudo journalctl -u camera-driver-installer
   ```

3. Verify the driver is properly installed:

   ```
   dpkg -l | grep tier4-camera-gmsl
   ```
