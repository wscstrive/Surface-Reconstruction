# Datasets
There are three mainstream datasets being used for Gaussian Splatting-based Surface Reconstruction: the DTU dataset, the Tanks and Temples dataset, and the Mip-NeRF 360 dataset, respectively.
> I will record where I got them from and how I converted them to the format suitable for SR models.  
> And also, I provided these three processed datasets in Google Drive. 

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
│   └── ...
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
### 1. We need to download the `dtu_dataset/dtu` file from 2DGS
### 2. We will download the `dtu_eval` files from the official MVS Data website.
- the ObsMask files
  - We need to download SampleSet.zip first
  - The ObsMask files can be found in SampleSet.zip's path (/SampleSet/MVS Data/ObsMask), so we can use code to unzip the ObsMask files only.
    ```shell
    # unzip absolute path only 
    unzip SampleSet.zip "SampleSet/MVS Data/ObsMask/*" -d ./dtu/dtu_eval/
    # then we need to use mv code to move ./dtu/dtu_eval/SampleSet/MVS Data/ObaMask to ./dtu/dtu_eval/, and use rm -rf code to delete SampleSet/MVS Data files
    mv ./dtu/dtu_eval/SampleSet/MVS\ Data/ObsMask/ ./dtu/dtu_eval/
    rm -rf dtu/dtu_eval/SampleSet/
    ```
- Points files can be found by downloading the Points.zip files from the MVS dataset website.
## Tanks and Temples dataset


## MipNeRF360 dataset
### The first Method. We will download the Mip-NeRF 360 dataset from [<u>the official website</u>](https://jonbarron.info/mipnerf360/)
- Dataset Pt.1 (__include__ bicycle, bonsai, counter, garden, kitchen, room, stump)
- Dataset Pt.2 (__include__ flowers, treehill) 
### The second method. We can download the processed Mip-NeRF 360 dataset from my Google Drive
- m360_dataset(__include__ bicycle, bonsai, counter, garden, kitchen, room, stump, flowers, treehill)
```
m360_dataset
├── bicycle
│   ├── images
│   │   ├── _DSC8679.JPG
│   │   ...
│   ├── images_2
│   ├── images_4
│   ├── images_8
│   ├── sparse
│   │    └── 0
│   │       ├── cameras.bin
│   │       ├── images.bin
│   │       └── points3d.bin
│   └── poses_bounds.npy
 ...
```
