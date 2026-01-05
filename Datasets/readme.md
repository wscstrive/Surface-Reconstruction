# Datasets
There are three mainstream datasets being used for Gaussian Splatting-based Surface Reconstruction: the DTU dataset, the Tanks and Temples dataset, and the Mip-NeRF 360 dataset, respectively.
> I will record where I got them from and how I converted them to the format suitable for SR models.  
> And also, I provided these three processed datasets in Google Drive.  
> 
- dtu_dataset
- tnt_dataset
- m360_dataset

The total dataset folder is like this:

```
datasets
├── dtu_dataset
│   ├── scan24
│   ...
├── tnt_dataset
│   ├── Barn
│   ...
└── m360_dataset
    ├── bicycle
    ...
```


## DTU dataset

```
dtu_dataset
├── dtu
│   ├── scan24
│   │   ├── depths
│   │   │   ├── 0000.pt
│   │   │   ...
│   │   ├── images
│   │   │   ├── 0000.png
│   │   │   ...
│   │   ├── mask
│   │   │   ├── 000.png
│   │   │   ...
│   │   ├── sparse
│   │   │   └── 0
│   │   │       ├── cameras.bin
│   │   │       ├── cameras.txt
│   │   │       ├── images.bin
│   │   │       ├── images.txt
│   │   │       ├── points3d.bin
│   │   │       ├── points3d.txt
│   │   │       └── points3d.ply
│   │   ├── cameras.npz
│   │   ├── database.db
│   │   └── points.ply
│   ...
└── dtu_eval
    ├── ObsMask
    │   ├── ObsMask1_10.mat
    │   ...
    │   ├── Plane1.mat
    │   ...
    └── Points
        └── stl
            ├── stl001_total.ply
            ...
```
### 1. Download the preprocessed training dataset `dtu_dataset/dtu` from [<u>2DGS</u>](https://github.com/hbb1/2d-gaussian-splatting/tree/main)
### 2. Download the official evaluate dataset `dtu_dataset/dtu_eval` from [<u>the official MVS Data website</u>](https://roboimagedata.compute.dtu.dk/?page_id=36) `SampleSet`.
- The ObsMask data (or __others__)
  - We need to download SampleSet.zip first
  - The ObsMask files can be found in SampleSet.zip's path (/SampleSet/MVS Data/ObsMask), so we can use code to unzip the ObsMask data only.
    ```shell
    # unzip absolute path only 
    unzip SampleSet.zip "SampleSet/MVS Data/ObsMask/*" -d ./dtu/dtu_eval/
    # then we need to use mv code to move ./dtu/dtu_eval/SampleSet/MVS Data/ObaMask to ./dtu/dtu_eval/, and use rm -rf code to delete SampleSet/MVS Data files
    mv ./dtu/dtu_eval/SampleSet/MVS\ Data/ObsMask/ ./dtu/dtu_eval/
    rm -rf dtu/dtu_eval/SampleSet/
    ```
- Points files can be found by downloading the `Points.zip` data from the MVS dataset website.
## Tanks and Temples dataset
### 1. Download preprocessed datas from [<u>the TNT official website</u>](https://www.tanksandtemples.org/download/).
- Training Data (ground truth, image set)
- `Results` on Training Data (Reconstruction, Camera Poses, Alignment, Cropfiles)
```
tnt_dataset
├── Barn
│   ├── images_raw
│   │   ├── 000001.jpg
│   │   ...
│   ├── Barn.json
│   ├── Barn.ply
│   ├── Barn_COLMAP_SfM.log
│   └── Barn_trans.txt
...
```
### 2. Follow the official website to install [<u>Colmap</u>](https://colmap.github.io/install.html).
```shell
# Colmap website
https://colmap.github.io/install.html
```
### 3. Use `preprocess/convert_tnt.py` to generate the related data, as shown below:
```
tnt_dataset
├── Barn
│   ├── images                  # custom resolution
│   │   ├── 000001.jpg
│   │   ...
│   ├── sparse                  # 3d points parameters
│   │   ├── 0
│   │   │   ├── camera.bin
│   │   │   ├── camera.txt
│   │   │   ├── images.bin
│   │   │   ├── images.txt
│   │   │   ├── Points3D.bin
│   │   │   └── Points3D.txt
│   ...
...
```
## MipNeRF360 dataset
### Download the Mip-NeRF 360 dataset from [<u>the official website</u>](https://jonbarron.info/mipnerf360/)
- Dataset Pt.1 (__include__ bicycle, bonsai, counter, garden, kitchen, room, stump)
- Dataset Pt.2 (__include__ flowers, treehill)
