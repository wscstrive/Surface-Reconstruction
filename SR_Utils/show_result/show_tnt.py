import os
import numpy as np

tnt_scenes = ['Barn', 'Caterpillar', 'Courthouse', 'Ignatius', 'Meetingroom', 'Truck']

output_dirs = ["/home/wangsc/Documents/SurR/outputs/output-2dgs/tnt"]
all_metrics = {"precision": [], "recall": [], "f-score": []}
print(output_dirs)

for scene in tnt_scenes:
    print(scene,end=" ")
    for output in output_dirs:
        # precision
        precision_file = np.loadtxt(os.path.join(output, scene, f"train/ours_30000/evaluation/{scene}.precision.txt"))
        precision = precision_file[len(precision_file) // 5]
        print(precision, end=" ")
        
        # recall
        recall_file = np.loadtxt(os.path.join(output, scene, f"train/ours_30000/evaluation/{scene}.recall.txt"))
        recall = recall_file[len(recall_file)//5]
        print(recall, end=" ")
        
        # f-score
        f_score = 2 * precision * recall / (precision + recall)
        print(f_score)

        all_metrics["precision"].append(precision)
        all_metrics["recall"].append(recall)
        all_metrics["f-score"].append(f_score)


        latex = []
        for k in ["precision","recall", "f-score"]:
            numbers = float(np.mean(all_metrics[k]))
            numbers = all_metrics[k] + [numbers]

            numbers = [f"{x:.2f}" for x in numbers]
            if k == "f-score":
                latex.extend(numbers)

        print(" & ".join(latex))
