import json
import numpy as np

outdoor_scenes = ['bicycle', 'flowers', 'garden', 'stump', 'treehill']
indoor_scenes = ['room', 'counter', 'kitchen', 'bonsai']

output_dirs = ["/home/wangsc/Documents/SurR/outputs/output-gof/m360"]

KEY = "ours_30000"
METRICS = ["PSNR", "SSIM", "LPIPS"]

def eval_split(split_name, scenes, output_dirs):
    metrics = {k: [] for k in METRICS}

    print(f"\n===== {split_name} =====")
    print(output_dirs)

    for scene in scenes:
        print(scene, end=" ")
        for output in output_dirs:
            json_file = f"{output}/{scene}/results.json"
            with open(json_file, "r") as f:
                data = json.load(f)

            data = data[KEY]

            for k in METRICS:
                metrics[k].append(data[k])
                print(f"{data[k]:.3f}", end=" ")
        print()

    # mean + latex
    latex_parts = []
    for k in METRICS:
        mean_val = float(np.asarray(metrics[k]).mean())
        print(f"{split_name} mean {k}: {mean_val}")
        if k == "PSNR":
            latex_parts.append(f"{mean_val:.2f}")
        else:
            latex_parts.append(f"{mean_val:.3f}")

    latex_line = " & ".join(latex_parts)
    print(f"{split_name} LaTeX: {latex_line}")
    return metrics, latex_line


outdoor_metrics, outdoor_latex = eval_split("outdoor", outdoor_scenes, output_dirs)
indoor_metrics, indoor_latex = eval_split("indoor", indoor_scenes, output_dirs)
