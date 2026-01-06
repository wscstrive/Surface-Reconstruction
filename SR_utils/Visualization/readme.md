Most methods just generate gt and rendering images, but we need to check the geometric information, e.g., depth, normal, depth_normal, and so on. The visual_map.py script can help generate any maps you need. 

- Firstly, move visual_map.py to the main path.
  - methods/Visualization/visual_map.py --> methods/visual_map.py
```shell
# enter visual folder
cd ../Visualization
# move visual_map.py
mv visual_map.py ../
```

- Secondly, update all path, e.g. {dataset}_output_path (training data) and {dataset}_map_path (visual path), in script_visual.py. Script_visual combines three datasets to generate all maps.
- Thirdly, run script_visual.py
```shell
run Visualization/script_visual.py --dtu {dtu_path} --tnt {tnt_path} --m360 {m360_path}
```
