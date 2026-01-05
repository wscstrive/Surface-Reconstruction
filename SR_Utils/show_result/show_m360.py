import json
import numpy as np

outdoor_scenes = ['bicycle', 'flowers', 'garden', 'stump', 'treehill']
indoor_scenes = ['room', 'counter', 'kitchen', 'bonsai']

m360_scenes = ['bicycle', 'flowers', 'garden', 'stump', 'treehill',     # outdoor
               'room', 'counter', 'kitchen', 'bonsai']                  # indoor


output_dirs = ["/home/wangsc/Documents/SurR/outputs/output-gof/m360"]
all_metrics = {"PSNR": [], "SSIM": [], "LPIPS": []}
print(output_dirs)

for scene in m360_scenes:
    print(scene,end=" ")
    for output in output_dirs:
        json_file = f"{output}/{scene}/results.json"
        data = json.load(open(json_file))
        data = data['ours_30000']
        
        for k in ["PSNR", "SSIM", "LPIPS"]:
            all_metrics[k].append(data[k])
            print(f"{data[k]:.3f}", end=" ")
    print()

    latex = []
    for k in ["PSNR", "SSIM", "LPIPS"]:
        numbers = np.asarray(all_metrics[k]).mean(axis=0).tolist()
        numbers = [numbers]
        if k == "PSNR":
            numbers = [f"{x:.2f}" for x in numbers]
        else:
            numbers = [f"{x:.3f}" for x in numbers]
        latex.extend(numbers)
    print(" & ".join(latex))