import argparse
import yaml

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", default="my_project", type=str, required=True, help="")
    parser.add_argument("--camera_name", default="", nargs="+", required=True, help="")
    parser.add_argument("--camera_setup_file", default="", nargs="+", required=True, help="")
    parser.add_argument("--intrinsics_file", default="", nargs="+", required=False, help="")

    return parser


def main():
    args = make_parser().parse_args()

    project_name = args.project_name
    camera_names = args.camera_name
    intrinsics_files = args.intrinsics_file

    for i, camera_name in enumerate(camera_names):  
        camera_individual_params_dir = "src/individual_params/individual_params/config/" + project_name + "/" + camera_name
  
        with open(camera_individual_params_dir+"/camera_info.yaml", 'r') as file:
            camera_info_yaml = yaml.safe_load(file)

        with open(intrinsics_files[i], 'r') as file:
            intrinsics = yaml.safe_load(file)

        camera_info_yaml["camera_matrix"] = intrinsics["camera_matrix"]
        camera_info_yaml["distortion_model"] = intrinsics["distortion_model"]
        camera_info_yaml["distortion_coefficients"] = intrinsics["distortion_coefficients"]
        camera_info_yaml["projection_matrix"] = intrinsics["projection_matrix"]
        camera_info_yaml["rectification_matrix"] = intrinsics["rectification_matrix"]

        with open(camera_individual_params_dir+"/camera_info.yaml", 'w') as outfile:
            yaml.dump(camera_info_yaml, outfile, default_flow_style=None)

if __name__ == "__main__":
    main()