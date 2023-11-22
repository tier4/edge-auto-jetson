import os
import argparse
import yaml
import shutil

DEFAULT_CAMERA_MATRIX = dict(
    rows = 3,
    cols = 3,
    data = [1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
)
DEFAULT_DISTORTION_MODEL = None
DEFAULT_DISTORTION_COEFFICIENTS = dict(
    rows = 1,
    cols = 5,
    data = [0.0, 0.0, 0.0, 0.0, 0.0],
)
DEFAULT_PROJECTION_MATRIX = dict(
    rows = 3,
    cols = 4,
    data = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]
)
DEFAULT_RECTIFICATION_MATRIX = dict(
    rows = 3,
    cols = 3,
    data = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
)

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", default="my_project", type=str, required=True, help="")
    parser.add_argument("--camera_name", default="", nargs="+", required=True, help="")
    parser.add_argument("--camera_setup_file", default="", nargs="+", required=True, help="")
    parser.add_argument("--camera_intrinsics_file", default="", nargs="+", required=False, help="")
    parser.add_argument("--lidar_name", default="", nargs="+", required=True, help="")
    parser.add_argument("--lidar_calibration_file", default="", nargs="+", required=False, help="")
    parser.add_argument("--extrinsic_calibration_file", default="", nargs="+", required=False, help="")

    return parser


# first assume no intrinsics
def generate_yaml_files(camera_setup_file, camera_name, intrinsics_file=None):
    with open(camera_setup_file, 'r') as file:
       camera_setup_params = yaml.safe_load(file)

    if not intrinsics_file:
        camera_info_yaml = dict(
            image_width = camera_setup_params["image_width"],
            image_height = camera_setup_params["image_height"],
            camera_name = camera_name,
            camera_matrix = DEFAULT_CAMERA_MATRIX,
            distortion_model = DEFAULT_DISTORTION_MODEL,
            distortion_coefficients = DEFAULT_DISTORTION_COEFFICIENTS,
            projection_matrix = DEFAULT_PROJECTION_MATRIX,
            rectification_matrix = DEFAULT_RECTIFICATION_MATRIX,
            )
    else:
        with open(intrinsics_file, 'r') as file:
            intrinsics = yaml.safe_load(file)

        camera_info_yaml = dict(
            image_width = camera_setup_params["image_width"],
            image_height = camera_setup_params["image_height"],
            camera_name = camera_name,
            camera_matrix = intrinsics["camera_matrix"],
            distortion_model = intrinsics["distortion_model"],
            distortion_coefficients = intrinsics["distortion_coefficients"],
            projection_matrix = intrinsics["projection_matrix"],
            rectification_matrix = intrinsics["rectification_matrix"],
            )

    trigger_params_yaml = {
        '/**' : dict(
            ros__parameters = dict(
                frame_rate = camera_setup_params["frame_rate"],
                phase = camera_setup_params["phase"],
                gpio = camera_setup_params["gpio"],
                cpu_core_id = camera_setup_params["cpu_core_id"],
            )
        )
    }
    

    v4l2_params_yaml = {
        '/**': dict(
            ros__parameters = dict(
                video_device = camera_setup_params['video_device'],
                output_encoding = camera_setup_params['output_encoding'],
                image_size = [camera_setup_params['image_width'], camera_setup_params['image_height']],
            )
        )
    }


    return camera_info_yaml, trigger_params_yaml, v4l2_params_yaml


def main():
    # avoid issue with yaml writing references instead of values to a file
    yaml.Dumper.ignore_aliases = lambda *args : True

    args = make_parser().parse_args()

    project_name = args.project_name
    camera_names = args.camera_name
    camera_setup_file = args.camera_setup_file
    intrinsics_file = args.camera_intrinsics_file
    lidar_names = args.lidar_name
    lidar_calibration_files = args.lidar_calibration_file # TODO
    extrinsic_calibration_files = args.extrinsic_calibration_file
    
    general_parameters = dict(
        jetson_id = None,
        live_sensor = None,
        perception = None,
        project_name = project_name,
        lidar_centerpoint = None, 
        voxel_grid_based_euclidean_cluster = None, 
        lidar_model = None, 
    )

    launch_params_yaml = general_parameters

    for i, camera_name in enumerate(camera_names):
        if intrinsics_file:
            camera_info_yaml, trigger_params_yaml, v4l2_params_yaml = generate_yaml_files(camera_setup_file[i], camera_name, intrinsics_file[i])
        else:
            camera_info_yaml, trigger_params_yaml, v4l2_params_yaml = generate_yaml_files(camera_setup_file[i], camera_name, None)

        camera_individual_params_dir = "src/individual_params/individual_params/config/" + project_name + "/" + camera_name
        os.makedirs(camera_individual_params_dir, exist_ok=True)
        with open(camera_individual_params_dir+"/camera_info.yaml", 'w') as outfile:
            yaml.dump(camera_info_yaml, outfile, default_flow_style=None)
        with open(camera_individual_params_dir+"/trigger.param.yaml", 'w') as outfile:
            yaml.dump(trigger_params_yaml, outfile, default_flow_style=False)
        with open(camera_individual_params_dir+"/v4l2_camera.param.yaml", 'w') as outfile:
            yaml.dump(v4l2_params_yaml, outfile, default_flow_style=None)
        
    for i, lidar_name in enumerate(lidar_names):
        lidar_individual_params_dir = "src/individual_params/individual_params/config/" + project_name + "/" + lidar_name
        os.makedirs(lidar_individual_params_dir, exist_ok=True)

        if lidar_calibration_files:
            shutil.copy(lidar_calibration_files[i], lidar_individual_params_dir+"/"+os.path.basename(lidar_calibration_files[i])) # TODO: worried about file extension not generalizing

    if extrinsic_calibration_files:
        for file in extrinsic_calibration_files:
            shutil.copy(file, "src/individual_params/individual_params/config/" + project_name + "/" + os.path.basename(file))

    with open(project_name + "_launch_params.yaml", 'w') as outfile:
        yaml.dump(launch_params_yaml, outfile)


if __name__ == "__main__":
    main()