import torch
from PIL import Image
import numpy as np
import cv2
import os
from tqdm import tqdm

# update paths based on different models
from scene import Scene, GaussianModel
from argparse import ArgumentParser
from gaussian_renderer import render
from utils.general_utils import safe_state
from arguments import ModelParams, PipelineParams, get_combined_args


def save_img_u8(img, pth):
  """Save an image (probably RGB) in [0, 1] to disk as a uint8 PNG."""
  with open(pth, 'wb') as f:
    Image.fromarray(
        (np.clip(np.nan_to_num(img), 0., 1.) * 255.).astype(np.uint8)).save(
            f, 'PNG')

def save_img_f32(depthmap, pth):
  """Save an image (probably a depthmap) to disk as a float32 TIFF."""
  with open(pth, 'wb') as f:
    Image.fromarray(np.nan_to_num(depthmap).astype(np.float32)).save(f, 'TIFF')

def visualize_depth(depth, depth_min=None, depth_max=None, inverse=True):
  """Visualize the depth map with colormap.
     Rescales the values so that depth_min and depth_max map to 0 and 1,
     respectively.
  """
  if isinstance(depth, torch.Tensor):
    depth = depth.detach().cpu().numpy()
  depth = depth.astype(np.float32)

  if inverse:
    depth = 1.0 / (depth + 1e-6)
  if depth_min is None:
    depth_min = np.percentile(depth, 2)
  if depth_max is None:
    depth_max = np.percentile(depth, 98)

  depth[depth < depth_min] = depth_min
  depth[depth > depth_max] = depth_max

  depth_scaled = (depth - depth_min) / (depth_max - depth_min)
  depth_scaled_uint8 = np.uint8(depth_scaled * 255)

  depth_color = cv2.applyColorMap(depth_scaled_uint8, cv2.COLORMAP_VIRIDIS)

  return depth_color


def render_set(map_path, name, iteration, views, gaussians, pipeline, background): #  kernel_size):
    # global render
    render_path = os.path.join(map_path, name, "ours_{}".format(iteration), "render")
    gt_path = os.path.join(map_path, name, "ours_{}".format(iteration), "gt")
    depth_path = os.path.join(map_path, name, "ours_{}".format(iteration), "depth")
    normal_path = os.path.join(map_path, name, "ours_{}".format(iteration), "normal")
    depth_normal_path = os.path.join(map_path, name, "ours_{}".format(iteration), "depth_normal")

    os.makedirs(gt_path, exist_ok=True)
    os.makedirs(render_path, exist_ok=True)
    os.makedirs(depth_path, exist_ok=True)
    os.makedirs(normal_path, exist_ok=True)
    os.makedirs(depth_normal_path, exist_ok=True)

    for idx, view in enumerate(tqdm(views, desc="Rendering progress")):
        ###  2dgs
        # all_maps = render(view, gaussians, pipeline, background)
        # gt_map = view.original_image[0:3, :, :]
        # render_map = all_maps["render"]
        # normal_map = torch.nn.functional.normalize(all_maps['rend_normal'], dim=0)
        # depth_map = all_maps['surf_depth']
        # depth_normal_map = all_maps['surf_normal']
        ###  gof
        # all_maps = render(view, gaussians, pipeline, background, kernel_size)["render"]
        # gt_map = view.original_image[0:3, :, :]
        # render_map = all_maps[:3,:,:]
        # normal_map = torch.nn.functional.normalize(all_maps[3:6,:,:], dim=0)
        # depth_map = all_maps[6:7, :, :]
        # from utils.depth_utils import depth_to_normal
        # depth_normal_map, _ = depth_to_normal(view, depth_map)
        # depth_normal_map = depth_normal_map.permute(2, 0, 1)
        ###  pgsr
        all_maps = render(view, gaussians, pipeline, background)
        gt_map, _ = view.get_image()
        render_map = all_maps["render"]
        normal_map = all_maps["rendered_normal"]
        depth_map = all_maps["plane_depth"]
        depth_normal_map = all_maps["depth_normal"]


        save_img_u8(gt_map.permute(1, 2, 0).cpu().numpy(), os.path.join(gt_path, '{0:05d}'.format(idx) + ".png"))
        save_img_u8(render_map.permute(1, 2, 0).cpu().numpy(), os.path.join(render_path, '{0:05d}'.format(idx) + ".png"))
        save_img_u8(normal_map.permute(1, 2, 0).detach().cpu().numpy() * 0.5 + 0.5, os.path.join(normal_path, 'normal_{0:05d}'.format(idx) + ".png"))
        save_img_u8(depth_normal_map.permute(1, 2, 0).cpu().numpy() * 0.5 + 0.5, os.path.join(depth_normal_path, 'depth_normal_{0:05d}'.format(idx) + ".png"))

        depth_map = visualize_depth(depth_map.permute(1, 2, 0).squeeze())
        cv2.imwrite(os.path.join(depth_path, 'depth_{0:05d}'.format(idx) + ".png"), depth_map)


def render_sets(dataset : ModelParams, iteration : int, pipeline : PipelineParams, map_path):
    with torch.no_grad():
        gaussians = GaussianModel(dataset.sh_degree)
        scene = Scene(dataset, gaussians, load_iteration=iteration, shuffle=False)

        bg_color = [1,1,1] if dataset.white_background else [0, 0, 0]
        background = torch.tensor(bg_color, dtype=torch.float32, device="cuda")
        print("start rendering train maps")
        render_set(map_path, "train", scene.loaded_iter, scene.getTrainCameras(), gaussians, pipeline, background) # kernel_size=dataset.kernel_size
        # print("start rendering test maps")
        # render_set(map_path, "test", scene.loaded_iter, scene.getTestCameras(), gaussians, pipeline, background)

if __name__ == "__main__":
    # Set up command line argument parser
    parser = ArgumentParser(description="Rendering all maps")
    model = ModelParams(parser, sentinel=True)
    pipeline = PipelineParams(parser)
    parser.add_argument("--iteration", default=-1, type=int)
    # parser.add_argument("--skip_train", action="store_true")
    # parser.add_argument("--skip_test", action="store_true")
    parser.add_argument("--map_path", '-p', required=True, type=str)
    parser.add_argument("--quiet", action="store_true")
    args = get_combined_args(parser)
    # import sys
    # args = parser.parse_args(sys.argv[1:])
    print("Rendering " + args.map_path)

    # Initialize system state (RNG)
    safe_state(args.quiet)

    render_sets(model.extract(args), args.iteration, pipeline.extract(args), args.map_path)
    print("Done.")