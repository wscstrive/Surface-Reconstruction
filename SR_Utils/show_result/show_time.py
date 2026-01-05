import os
import json
import numpy as np

BASE_DIR = "/home/wangsc/Documents/SurR/outputs/output-gof/dtu/"

times_min = []

def parse_time_to_minutes(time_str):
    """
    支持:
    - HH:MM:SS
    - MM:SS
    - SS
    返回: 分钟(float)
    """
    parts = time_str.strip().split(":")
    parts = [float(p) for p in parts]

    if len(parts) == 3:       # HH:MM:SS
        h, m, s = parts
        total_sec = h * 3600 + m * 60 + s
    elif len(parts) == 2:     # MM:SS
        m, s = parts
        total_sec = m * 60 + s
    elif len(parts) == 1:     # SS
        total_sec = parts[0]
    else:
        raise ValueError(f"Invalid time format: {time_str}")

    return total_sec / 60.0


for scene in os.listdir(BASE_DIR):
    scene_dir = os.path.join(BASE_DIR, scene)
#     scene_dir = os.path.join(scene_dir, "test")
    json_path = os.path.join(scene_dir, "training_time.json")

    if not os.path.isfile(json_path):
        continue

    try:
        with open(json_path, "r") as f:
            data = json.load(f)

        time_str = data.get("training_time", None)
        if time_str is None:
            print(f"[WARN] {scene}: no 'training_time'")
            continue

        t_min = parse_time_to_minutes(time_str)
        times_min.append(t_min)

        print(f"[OK] {scene}: {t_min:.2f} min")

    except Exception as e:
        print(f"[ERROR] {scene}: {e}")

# ===== 统计 =====
if times_min:
    avg_min = np.mean(times_min)

    print("\n======================")
    print(f"Total scenes: {len(times_min)}")
    print(f"Average training time: {avg_min:.2f} min")
    print("======================")
else:
    print("No valid training_time.json found!")
