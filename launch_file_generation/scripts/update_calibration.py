import argparse
import yaml
import os
import shutil

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", default="my_project", type=str, required=True, help="")
    parser.add_argument("--camera_names", default="", nargs="+", required=False, help="")
    parser.add_argument("--camera_intrinsics_files", default="", nargs="+", required=False, help="")
    parser.add_argument("--lidar_name", default="", nargs="+", required=False, help="")
    parser.add_argument("--lidar_calibration_file", default="", nargs="+", required=False, help="")
    parser.add_argument("--extrinsic_calibration_files", default="", nargs="+", required=False, help="")

    return parser


def main():
    args = make_parser().parse_args()

    project_name = args.project_name
    camera_names = args.camera_names
    camera_intrinsics_files = args.camera_intrinsics_files
    lidar_name = args.lidar_name
    lidar_calibration_file = args.lidar_calibration_file 
    extrinsic_calibration_files = args.extrinsic_calibration_file

    for i, camera_name in enumerate(camera_names):  
        camera_individual_params_dir = "src/individual_params/individual_params/config/" + project_name + "/" + camera_name
  
        with open(camera_individual_params_dir+"/camera_info.yaml", 'r') as file:
            camera_info_yaml = yaml.safe_load(file)

        with open(camera_intrinsics_files[i], 'r') as file:
            intrinsics = yaml.safe_load(file)

        camera_info_yaml["camera_matrix"] = intrinsics["camera_matrix"]
        camera_info_yaml["distortion_model"] = intrinsics["distortion_model"]
        camera_info_yaml["distortion_coefficients"] = intrinsics["distortion_coefficients"]
        camera_info_yaml["projection_matrix"] = intrinsics["projection_matrix"]
        camera_info_yaml["rectification_matrix"] = intrinsics["rectification_matrix"]

        with open(camera_individual_params_dir+"/camera_info.yaml", 'w') as outfile:
            yaml.dump(camera_info_yaml, outfile, default_flow_style=None)

    lidar_individual_params_dir = "src/individual_params/individual_params/config/" + project_name + "/" + lidar_name
    os.makedirs(lidar_individual_params_dir, exist_ok=True)

    if lidar_calibration_file:
        shutil.copy(lidar_calibration_file, lidar_individual_params_dir+"/"+os.path.basename(lidar_calibration_file))

    if extrinsic_calibration_files:
        for file in extrinsic_calibration_files:
            shutil.copy(file, "src/individual_params/individual_params/config/" + project_name + "/" + os.path.basename(file))

if __name__ == "__main__":
    main()