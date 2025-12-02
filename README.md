# Introduction

This repository is my personal research notebook.  
It serves as a collection of surface-reconstruction–related papers that I come across anytime and anywhere.

## Paper lists
> This repo. just roughly records the contributions of each paper (Why->What->How). My notes are mainly recorded on Notion.

![Static Badge](https://img.shields.io/badge/Surface_Reconstruction-%E8%9C%98%E8%9B%9B%E7%A7%91%E5%AD%A6%E5%AE%B6-critical?style=flat&logo=notion&labelColor=auto&link=https%3A%2F%2Fwww.notion.so%2FNotes-2b13db23b7038076a17bef7408d980e7%3Fsource%3Dcopy_link)



- __SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering.__ _Antoine Guédon, Vincent Lepetit._ __CVPR, 2024.__ [[`Paper`](https://arxiv.org/pdf/2311.12775)] [[`Code`](https://github.com/Anttwo/SuGaR)] (★★☆☆☆)(No reading code)
  - To reduce interference from overlapping Gaussians, the Gaussian nearest to the point $p$ is selected. \
    The SDF is then defined by shortening the distance along its smallest scale axis, and this estimated SDF is regularized toward the ground-truth SDF to achieve surface alignment.

- __2D Gaussian Splatting for Geometrically Accurate Radiance Fields.__ _Binbin Huang et.al._  __SIGGRAPH, 2024.__ [[`Paper`](https://arxiv.org/pdf/2403.17888)] [[`Code`](https://github.com/hbb1/2d-gaussian-splatting)] (★★★★☆)
  - __Initialize 2D Gaussian primitives__ to ensure multi-view consistency, and use __homogeneous transformations__ to remove the errors introduced by affine projection approximations.

- __High-quality Surface Reconstruction using Gaussian Surfels.__ _Pinxuan Dai, Jiamin Xu et.al._ __SIGGRAPH, 2024.__ [[`Paper`](https://arxiv.org/pdf/2404.17774)] [[`Code`](https://github.com/turandai/gaussian_surfels)] (★★★★☆)
  - Introduces Gaussian surfels (with scale.z = 0) and __adaptively adjusts pixel-wise depths__ when the surfels align with slanted surfaces.
  
- __GSDF: 3DGS Meets SDF for Improved Neural Rendering and Reconstruction.__ _Mulin Yu et.al._  __NeurIPS, 2024.__ [[`Paper`](https://arxiv.org/pdf/2403.16964)] [[`Code`](https://github.com/city-super/GSDF)] [[`Note`]()] (Unread)

- __GS2Mesh: Surface Reconstruction from Gaussian Splatting via Novel Stereo Views.__ _Yaniv Wolf et.al._ __ECCV, 2024.__ [[`Paper`](https://arxiv.org/pdf/2404.01810)] [[`Code`](https://github.com/yanivw12/gs2mesh/tree/main)] [[`Note`]()] (Unread)

- __Gaussian Opacity Fields: Efficient Adaptive Surface Reconstruction in Unbounded Scenes.__ _Zehao Yu et.al._ __TOG, 2024.__ [[`Paper`](https://arxiv.org/pdf/2404.10772)] [[`Code`](https://github.com/autonomousvision/gaussian-opacity-fields)] [[`Note`]()] (★★★☆☆)

- __RaDe-GS: Rasterizing Depth in Gaussian Splatting.__ _Baowen Zhang et.al._ __ArXiv, 2024.__ [[`Paper`](https://arxiv.org/pdf/2406.01467)] [[`Code`](https://github.com/HKUST-SAIL/RaDe-GS)] [[`Note`]()] (Unread)

- __3DGSR: Implicit Surface Reconstruction with 3D Gaussian Splatting.__ _XIAOYANG LYU et.al._ __TOG, 2024__ [[`Paper`](https://arxiv.org/pdf/2404.00409)] [`No Code`] [[`Note`]()] (★☆☆☆☆)
  - 123
    - 123

- __Surface Reconstruction from 3D Gaussian Splatting via Local Structural Hints.__ _Qianyi Wu et.al._ __ECCV, 2024__ [[`Paper`](https://wuqianyi.top/media/GSRec.pdf)] [[`Code`](https://github.com/QianyiWu/gsrec)] [[`Note`]()] (Unread)

- __PGSR: Planar-based Gaussian Splatting for Efficient and High-Fidelity Surface Reconstruction.__ _Danpeng Chen et.al._ __TVCG, 2024__ [[`Paper`](https://arxiv.org/pdf/2406.06521)] [[`Code`](https://github.com/zju3dv/PGSR)] [[`Note`]()] (★★★☆☆)

- __Trim 3D Gaussian Splatting for Accurate Geometry Representation.__ _Lue Fan, Yuxue Yang et.al._ __ArXiv, 2024.__ [[`Paper`](https://arxiv.org/pdf/2406.07499)] [[`Code`](https://github.com/YuxueYang1204/TrimGS)] [[`Note`]()] (Unread)

- __MonoGSDF: Exploring Monocular Geometric Cues for Gaussian Splatting-Guided Implicit Surface Reconstruction.__ _Kunyi Li et.al._ __ArXiv, 2024.__ [[`Paper`](https://arxiv.org/pdf/2411.16898)] [`No Code`] [[`Note`]()] (Unread)

- __SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction.__ _Mulin Yu et.al._  __NeurIPS, 2024.__ [[`Paper`](https://arxiv.org/pdf/2412.15400)] [`No Code`] [[`Note`]()] (Unread)

- __GausSurf: Geometry-Guided 3D Gaussian Splatting for Surface Reconstruction.__ _Jiepeng Wang et.al._ __ArXiv, 2024.__ [[`Paper`](https://arxiv.org/pdf/2411.19454)] [[`Code`](https://github.com/jiepengwang/GausSurf)] ([`Note`]()) (Unread)

- __αSurf: Implicit Surface Reconstruction for Semi-Transparent and Thin Objects with Decoupled Geometry and Opacity .__ _Keyang Ye et.al._ __3DV, 2025.__ [[`Paper`](https://arxiv.org/pdf/2303.10083)] [[`Code`](https://github.com/ChikaYan/alphasurf)] [[`Note`]()] (Unread)

- __Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views.__ _Jiang Wu et.al._ __CVPR, 2025.__ [[`Paper`](https://arxiv.org/pdf/2504.20378)] [[`Code`](https://github.com/Wuuu3511/Sparse2DGS)] [[`Note`]()] (Unread)

- __Volumetric Surfaces: Representing Fuzzy Geometries with Layered Meshes.__ _Stefano Esposito et.al._ __CVPR, 2025.__ [[`Paper`](https://arxiv.org/pdf/2409.02482)] [[`Code`](https://github.com/autonomousvision/volsurfs/tree/main)] [[`Note`]()] (Unread)

- __FatesGS: Fast and Accurate Sparse-View Surface Reconstruction Using Gaussian Splatting with Depth-Feature Consistency.__ _Han Huang, Yulun Wu et.al._ __AAAI, 2025 Oral.__ [[`Paper`](https://arxiv.org/pdf/2501.04628)] [[`Code`](https://github.com/yulunwu0108/FatesGS)] [[`Note`]()] (Unread)

- __Sparis: Neural Implicit Surface Reconstruction of Indoor Scenes from Sparse Views.__ _Yulun Wu, Han Huang et.al._ __AAAI, 2025 Oral.__ [[`Paper`](https://arxiv.org/pdf/2501.01196)] [[`Code`](https://github.com/yulunwu0108/Sparis/tree/master)] [[`Note`]()] (Unread)

- __When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering.__ _Keyang Ye et.al._ __TOG, 2025.__ [[`Paper`](https://arxiv.org/pdf/2504.17545)] [`No Code`] [[`Note`]()] (Unread)

- __Quadratic Gaussian Splatting: High Quality Surface Reconstruction with Second-order Geometric Primitives.__ _Ziyu Zhang, Binbin Huang et.al._  __ICCV, 2025.__ [[`Paper`](https://arxiv.org/pdf/2411.16392)] [[`Code`](https://github.com/will-zzy/QGS)] [[`Note`]()] (★★★★☆)

- __MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions.__ _Qingyuan Zhou et.al._ __ICCV, 2025.__ [[`Paper`](https://arxiv.org/pdf/2503.05182)] [[`Code`](https://github.com/TsingyuanChou/MGSR)] [[`Note`]()] (Unread)

- __SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting.__ _Zihui Gao, Jia-Wang Bian et.al._ __ICCV, 2025.__ [[`Paper`](https://arxiv.org/pdf/2507.15602)] [[`Code`](https://github.com/aim-uofa/SurfaceSplat)] [[`Note`]()] (Unread)

- __PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface Reconstruction.__ _Yufei Han et.al._ __ICCV, 2025.__ [[`Paper`](https://arxiv.org/pdf/2509.19726)] [[`Code`](https://github.com/PRIS-CV/PolGS)] [[`Note`]()] (Unread)

- __MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient Surface Reconstruction.__ _Antoine Guédon, Diego Gomez et.al._ __TOG, 2025.__ [[`Paper`](https://arxiv.org/pdf/2506.24096)] [[`Code`](https://github.com/Anttwo/MILo)] [[`Note`]()] (Unread)

- __Multi-view Normal and Distance Guidance Gaussian Splatting for Surface Reconstruction.__ _Bo Jia et.al._ __ArXiv, 2025.__ [[`Paper`](https://arxiv.org/pdf/2508.07701)] [[`Code`](https://github.com/Bistu3DV/MND-GS)] [[`Note`]()] (Unread)

- __Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning.__ _Wenzhi Guo et.al._ __ArXiv, 2025.__ [[`Paper`](https://arxiv.org/pdf/2509.07493)] [[`Code`](https://github.com/DARYL-GWZ/DIGS)] [[`Note`]()] (Unread)

- __GS-2M: Gaussian Splatting for Joint Mesh Reconstruction and Material Decomposition.__ _D. M. Nguyen et.al._ __ArXiv, 2025.__ [[`Paper`](https://arxiv.org/pdf/2509.22276)] [[`Code`](https://github.com/ndming/GS-2M/tree/main)] [[`Note`]()] (Unread)


- __GVKF: Gaussian Voxel Kernel Functions for Highly Efficient Surface Reconstruction in Open Scenes.__ _Gaochao Song, Chong Cheng et.al._ __NeurIPS, 2025.__ [[`Paper`](https://arxiv.org/pdf/2411.01853)] [[`Code`](https://github.com/3DAgentWorld/GVKF/tree/main)] [[`Note`]()]


## Extension

