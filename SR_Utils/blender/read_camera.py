## 在blender的scripts中渲染图像

import bpy, math

# ========= 1) 相机参数 =========

cam_loc = (
-2.247744417912683, -0.25676986688509823, 3.3975459057555306
)
cam_rot_deg = (
341.99101750638033, 25.707031618386132, 178.7859940647626
)  # Euler XYZ, degrees

focal_mm = 21.38         # Focal Length
shift_x, shift_y = 0.0, 0.0
clip_start, clip_end = 0.1, 100.0

# 分辨率（可选）
res_x, res_y = 979, 545

# ========= 2) 灯光参数（Point Light） =========
light_name   = "Light"
light_type   = "POINT"     # 'POINT' / 'SUN' / 'SPOT' / 'AREA'
light_loc    = (
-2.247744417912683, -0.25676986688509823, 3.3975459057555306
)
light_rot_deg= (
341.99101750638033, 25.707031618386132, 178.7859940647626
)  # 对 POINT 旋转无效
power        = 110      # Power / Energy
normalize    = True        # 仅对支持的光型设置（AREA/部分版本的SPOT）
radius       = 0.1         # 阴影软硬 (shadow_soft_size)
use_shadow   = True        # 勾选 Shadow

# ========= 工具函数 =========
def deg2rad(e): return tuple(math.radians(v) for v in e)

def ensure_camera():
    cam = bpy.context.scene.camera
    if cam is None:
        for ob in bpy.context.scene.objects:
            if ob.type == 'CAMERA':
                bpy.context.scene.camera = ob
                return ob
        cam_data = bpy.data.cameras.new("Camera")
        cam = bpy.data.objects.new("Camera", cam_data)
        bpy.context.scene.collection.objects.link(cam)
        bpy.context.scene.camera = cam
    return cam

def ensure_light(name, ltype='POINT'):
    ob = bpy.data.objects.get(name)
    if ob and ob.type == 'LIGHT':
        ob.data.type = ltype
        return ob
    ldat = bpy.data.lights.new(name=name, type=ltype)
    ob = bpy.data.objects.new(name, ldat)
    bpy.context.scene.collection.objects.link(ob)
    return ob

# ========= 相机 =========
cam = ensure_camera()
cam.rotation_mode = 'XYZ'
cam.location = cam_loc
cam.rotation_euler = deg2rad(cam_rot_deg)

cd = cam.data
cd.type = 'PERSP'
cd.lens = focal_mm
cd.lens_unit = 'MILLIMETERS'
cd.shift_x = shift_x
cd.shift_y = shift_y
cd.clip_start = clip_start
cd.clip_end = clip_end

# 可选分辨率
scene = bpy.context.scene
scene.render.resolution_x = res_x
scene.render.resolution_y = res_y

# ========= 灯光 =========
Lobj = ensure_light(light_name, light_type)
Lobj.location = light_loc
Lobj.rotation_mode = 'XYZ'
Lobj.rotation_euler = deg2rad(light_rot_deg)  # 对 POINT 不起作用，保留无害

L = Lobj.data
L.type = light_type
L.energy = power
L.shadow_soft_size = radius
L.use_shadow = use_shadow

# 只有在支持的光型/版本上才设置 use_normalized，避免报错
if hasattr(L, "use_normalized") and light_type in {"AREA", "SPOT"}:
    L.use_normalized = normalize

print("[OK] Camera & Light updated without errors.]")

## 从json文件中提取信息，并将旋转矩阵转换成blender的欧拉角
import json
from scipy.spatial.transform import Rotation as R

# ✅ 你提供的旋转转欧拉函数
def rot_2_euler_in_blender(rotation_matrix):
    r = R.from_matrix(rotation_matrix)
    eu = r.as_euler('xyz', degrees=True)
    eu[0] = eu[0] + 180  # X 加 180°
    return eu


def print_all_cameras(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    def process_obj(obj):
        if isinstance(obj, dict) and "rotation" in obj and "id" in obj:
            print("\n=======================================")
            print(f"📌 Camera id: {obj['id']}")
            print(json.dumps(obj, indent=4, ensure_ascii=False))

            rot = obj["rotation"]
            euler = rot_2_euler_in_blender(rot)

            print("\n🎯 Euler XYZ (Degrees)：")
            print(f"X = {euler[0]}")
            print(f"Y = {euler[1]}")
            print(f"Z = {euler[2]}")
            print("=======================================\n")

        if isinstance(obj, dict):
            for v in obj.values():
                process_obj(v)
        elif isinstance(obj, list):
            for v in obj:
                process_obj(v)

    process_obj(data)


if __name__ == "__main__":
    json_file = "/media/wangsc/T7/outputs/2dgs/outputs/dtu/scan105/cameras.json"
    print_all_cameras(json_file)
