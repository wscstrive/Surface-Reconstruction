import os
from argparse import ArgumentParser

####################### DTU #######################
dtu_scenes = ['scan24', 'scan37', 'scan40', 'scan55', 'scan63', 'scan65', 'scan69', 'scan83', 'scan97', 'scan105',
              'scan106', 'scan110', 'scan114', 'scan118', 'scan122']

parser = ArgumentParser(description="Rendering all maps")
parser.add_argument("--dtu_output_path", default="/home/wangsc/Documents/SurR/outputs/output-pgsr/dtu")
parser.add_argument('--dtu_map_path', default="/home/wangsc/Documents/SurR/outputs/visual-pgsr/dtu")
parser.add_argument('--dtu', "-dtu", required=True, type=str)
args, _ = parser.parse_known_args()

all_scenes = []
all_scenes.extend(dtu_scenes)

common_args = " --quiet"
for scene in dtu_scenes:
    source = args.dtu + "/" + scene
    print("python visual_map.py --iteration 30000 -s " + source + " -m " + args.dtu_output_path + "/" + scene + "/test" + " -p "  + args.dtu_map_path + "/" + scene)
    os.system("python visual_map.py --iteration 30000 -s " + source + " -m " + args.dtu_output_path + "/" + scene + "/test" + " -p " + args.dtu_map_path + "/" + scene)


####################### TNT #######################
tnt_datasets = ['Barn', 'Caterpillar', 'Ignatius', 'Truck', 'Meetingroom', 'Courthouse']
parser = ArgumentParser(description="Rendering all maps")
parser.add_argument("--tnt_output_path", default="/home/wangsc/Documents/SurR/outputs/output-pgsr/tnt")
parser.add_argument('--tnt_map_path', default="/home/wangsc/Documents/SurR/outputs/visual-pgsr/tnt")
parser.add_argument('--tnt', "-tnt", required=True, type=str)
args, _ = parser.parse_known_args()

all_tnt_scenes = []
all_tnt_scenes.extend(tnt_datasets)

for scene in all_tnt_scenes:
    source = args.tnt + "/" + scene
    print("python visual_map.py --iteration 30000 -s " + source + " -m " + args.tnt_output_path + "/" + scene + "/test" + " -p "  + args.tnt_map_path + "/" + scene)
    os.system("python visual_map.py --iteration 30000 -s " + source + " -m " + args.tnt_output_path + "/" + scene + "/test" + " -p " + args.tnt_map_path + "/" + scene)


####################### M360 #######################
m360_datasets = ["bicycle", "flowers", "garden", "stump", "treehill", "room", "counter", "kitchen", "bonsai"]
parser = ArgumentParser(description="Rendering all maps")
parser.add_argument("--m360_output_path", default="/home/wangsc/Documents/SurR/outputs/output-pgsr/m360")
parser.add_argument('--m360_map_path', default="/home/wangsc/Documents/SurR/outputs/visual-pgsr/m360")
parser.add_argument('--m360', "-m360", required=True, type=str)
args, _ = parser.parse_known_args()

all_m360_scenes = []
all_m360_scenes.extend(m360_datasets)

for scene in all_m360_scenes:
    source = args.m360 + "/" + scene
    print("python visual_map.py --iteration 30000 -s " + source + " -m " + args.m360_output_path + "/" + scene + "/test" + " -p "  + args.m360_map_path + "/" + scene)
    os.system("python visual_map.py --iteration 30000 -s " + source + " -m " + args.m360_output_path + "/" + scene + "/test" + " -p " + args.m360_map_path + "/" + scene)