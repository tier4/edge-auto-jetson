from lxml import etree
import yaml
import os
import copy
import re
import argparse

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", default="my_project", type=str, required=True, help="")

    return parser

def replace_root_args(launch_file, params): # TODO: only replace outside layer of args
    launch_file_root = launch_file.getroot()
    
    # print(list(launch_file_root))
    for child in list(launch_file_root):
        if child.tag != "arg":
            continue
        # print(child.get("name"))
        if child.get("name") in params:
            child.set("default", str(params[child.get("name")]))

    return launch_file

def remove_extra_code(launch_file, device_params): # remove lines following "if false"
    for node in launch_file.iter():
        for field in node.keys():
            if field != "if":
                continue

            var_match = re.search("\$\(var .*?\)", node.get(field))
            if not var_match:
                continue

            if ("lidar_centerpoint" in var_match.group() or "voxel_grid_based_euclidean_cluster" in var_match.group()) and device_params[node.get(field)[var_match.span()[0]+6:var_match.span()[1]-1]] == False: # dead code
                print("removing node...")
                node.getparent().remove(node.getprevious()) # remove comment
                node.getparent().remove(node) # remove content
    
    return launch_file


def build_top_level_launcher(template, params):
    print("Generating top level launcher...")

    top_level_launch = replace_root_args(template, params)
    
    return top_level_launch
    

def build_perception_launcher(camera_template, lidar_template, params):
    print("Generating perception launcher...")

    # get device names
    project_path = "src/individual_params/individual_params/config/" + params["project_name"]
    device_names = [dir for dir in os.listdir(project_path) if os.path.isdir(os.path.join(project_path, dir))]

    launch_root = etree.Element("launch")
    camera_id = 0
    for i, device_name in enumerate(device_names):
        if "camera_info.yaml" in os.listdir(project_path + "/" + device_name): # camera   
            print("camera...")
            camera_launch = copy.deepcopy(camera_template)

            params["camera_name"] = device_name
            params["camera_id"] = camera_id
            camera_id += 1

            camera_launch = replace_root_args(camera_launch, params)

            launch_root.append(camera_launch.getroot())

        else: # lidar TODO: is this a safe assumption?
            print("lidar...")
            lidar_launch = copy.deepcopy(lidar_template)
            
            params["lidar_name"] = device_name

            lidar_launch = replace_root_args(lidar_launch, params)

            # TODO: remove all nodes following "if false"
            lidar_launch = remove_extra_code(lidar_launch, params)

            launch_root.append(lidar_launch.getroot())

    return etree.ElementTree(launch_root)


def main():
    args = make_parser().parse_args()
    project_name = args.project_name

    # load parameters
    launch_params_file = project_name+"_launch_params.yaml"
    with open(launch_params_file, 'r') as file:
        launch_params = yaml.safe_load(file)

    # load top level launcher template
    top_level_template = etree.parse("edge_auto_jetson_template.launch.xml")
    
    # build top level launcher
    top_level_launcher = build_top_level_launcher(top_level_template, launch_params)

    # load template camera/lidar launch files
    camera_template = etree.parse("camera_template.launch.xml")
    lidar_template = etree.parse("lidar_template.launch.xml")

    # build perception launcher
    perception_launcher = build_perception_launcher(camera_template, lidar_template, launch_params)

    # write launchers to files
    top_level_launcher.write('src/launcher/edge_auto_jetson_launch/launch/'+project_name+'_edge_auto_jetson.launch.xml', pretty_print=True)
    perception_launcher.write('src/launcher/edge_auto_jetson_launch/launch/'+project_name+'_perception_jetson'+str(launch_params['jetson_id'])+'.launch.xml', pretty_print=True)


if __name__ == "__main__":
    main()



# helper functions
# def FILE(v):
#     return {'file': v}

# def NAME(v):
#     return {'name': v}

# def VALUE(v):
#     return {'value': v}

# def replace_root_args(launch_file, params):
#     for arg in launch_file.iterfind(".//arg"):
#         # print("arg name = ", arg.get("name"))
#         if arg.get("name") in params.keys():
#             # print("params[arg.get(\"name\")] = ", params[arg.get("name")])
#             arg.set("value", params[arg.get("name")])

#     return launch_file

# def replace_vars(launch_file, params):
#     for node in launch_file.iter():
#         for field in node.keys():
#             var_match = re.search("\$\(var .*?\)", node.get(field))
#             while var_match:
#                 new_value = node.get(field).replace(var_match.group(), str(params[node.get(field)[var_match.span()[0]+6:var_match.span()[1]-1]]))
#                 node.set(field, new_value)

#                 params[node.get("name")] = node.get(field)

#                 var_match = re.search("\$\(var .*?\)", node.get(field))

#     return launch_file

# def clean_file(launch_file):
#     for node in launch_file.iter():
#         for field in node.keys():
#             if field == "if" and node.get(field) == "false":
#                 parent = node.get_parent()
#                 parent.remove(node)
