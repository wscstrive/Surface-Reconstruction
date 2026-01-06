The results for each dataset in papers are the average result of all scenes, so three scripts are introduced to quickly compile the average results for all scenes. (from pgsr)  
And also, the training time script is introduced to compile average training time of all scenes.

## Show_dtu
The `{path_to}/results.json` of each scene can be got after all steps. The __Mean__ (overall) of all scenes can be accessed by running `show_dtu.py`.
```shell
# result.json
{
 "mean_d2s": ###,
 "mean_s2d": ###,
 "overall": ###
}

# run script. you need to change your path
python run_dtu.py 
```

## show_tnt
The __Mean__ of tnt datasets is the average result of precision and recall across all scenes. 
```shell
# run script
python run_tnt.py
```
## show_m360
```shell
# run script
python run_m360.py
```
## show_time
Firstly, we need add the following script into the training code.
```shell
if iteration == opt.iterations:

    # ----------record training time
    import json
    time = progress_bar.format_dict["elapsed"]
    time_path = os.path.join(dataset.model_path, "training_time.json")
    with open(time_path, "w") as f:
        json.dump({"training_time": progress_bar.format_interval(time)},f,indent=4)
    # ----------
    
    progress_bar.close()
```
Then, we can get `training_time.json` after the training ends and run the time script to access the average training time of all scenes.
```shell
# training_time.json
{
    "training_time": "##:##"
}

# run script
run show_time.py
```
