# 3D-model-seafloor-benchmark-by-SfM
## 1. Introduction
### 1.1 Marine geodesy
Marine geodesy focuses on studying seafloor crustal deformation, which spans approximately 70% of the Earth’s surface. However, conventional satellite-based geodetic techniques like GPS or InSAR cannot measure seafloor deformation since electromagnetic waves cannot penetrate water to significant depths due to substantial attenuation. Fortunately, over the past three decades, seafloor geodetic techniques have advanced to a level comparable to those implemented on land. Many seafloor geodetic techniques are now widely used, including acoustic ranging, fiber-optic strain sensors, repeat active-source sonar, seismic surveying, and continuous pressure-sensor monitoring of vertical motions (Bürgmann & Chadwell, 2014).


A pressure sensor detects vertical displacement by measuring changes in seawater pressure. Since seawater is much denser than air, even a small depth difference results in a significant pressure change. A seafloor benchmark or monument is used as a reference point for measuring pressure. This approach is commonly implemented in subduction zones (e.g., Ballu et al., 2013; Cook et al., 2023).  

### 1.2 Importance of seafloor benchmarks 
Seafloor pressure is a key indicator of seafloor height, so it is essential to account for pressure variations caused by oceanic and atmospheric conditions. Standard pressure gauges are unreliable and need self-calibration to improve the accuracy for long-term measurements (months to years) due to inherent drift (Polster et al., 2009). Several methods address this drift, including mobile pressure recorder (MPR) surveys, mobile pressure calibrator surveys, standard self-calibrating pressure recorders (SCPRs), and A0A sensors. These approaches continuously monitor and measure relative pressure changes.


Instead, the Absolute Self-Calibrating Pressure Recorder (ASCPR) measures absolute pressure at each benchmark through campaign-style deployments. The ASCPR is transported and operated by an ROV, placed on a permanent seafloor benchmark, and records both ocean and reference pressures for several hours (Cook et al., 2023).
 
### 1.3 Introduction to structure-from-motion (SfM) 
Structure-from-Motion (SfM) is a photogrammetric technique that generates 3D structures from a series of overlapping and offset images. Unlike traditional photogrammetry, SfM processes unordered image sets and does not rely on prior knowledge of camera positions or scene geometry. Instead, it simultaneously determines these parameters by automatically detecting matching features across multiple images and performing bundle adjustments. Consequently, 3D point clouds are constructed in a relative coordinate system, which requires alignment to real physical objects for scaling correction (Westoby et al., 2012; Schonberger & Frahm, 2016).


SfM employs the Scale-Invariant Feature Transformation (SIFT) algorithm to identify common features across all images for image correspondence (Lowe, 2004). Keypoint identification is then refined through bundle adjustment to construct a sparse point cloud, including camera positions and orientations (Snavely et al., 2008). Additionally, tracks—connected sets of matching features across multiple photos—are retained if they contain at least two key points (Snavely et al., 2006). This process enables the removal of transient features, non-static objects, or unintentionally captured artifacts before rendering the 3D model. Finally, triangulation is utilized to estimate 3D point positions and reconstruct scene geometry (Westoby et al., 2012).


Despite being an inexpensive and user-friendly photogrammetric method for capturing topography, SfM is primarily effective for land or aerial surveys and provides high-resolution topographic mapping and spatial models. Notably, SfM achieves decimeter-scale vertical accuracy for complex topography, making it promising for geoscience applications. SfM has been widely deployed to survey various landforms, such as coastal cliffs, moraine-dam complexes, and glacially sculpted bedrock ridges (Westoby et al., 2012). These surveys indicate that SfM is a reliable terrestrial data collection method and a practical solution for inaccessible or remote areas. However, its application to the seafloor remains limited.


Some studies (e.g., David et al., 2021) have demonstrated the potential of using SfM Multi-View Stereo (SfM-MVS) techniques for shallow-water surveys by applying the algorithm to aerial photos captured by Unmanned Aerial Vehicles (UAVs). SfM-MVS has shown promise in reconstructing shallow-water (< 1m depth) reefs, especially in clear waters with low wave activity, though nonlinear distortions caused by water refraction must be accounted for. SfM can also achieve high spatial resolution for bathymetric modeling. For example, Storlazzi et al. (2016) utilized SfM to measure benthic complexity or rugosity in coral reef environments, comparing it with traditional methods like the chain-and-tape technique. Notably, uncalibrated video applications of SfM have demonstrated potential for creating more effective and quantitatively robust bathymetric models.

### 1.4 Research questions
One critical factor affecting the uncertainty of seafloor crustal movement measurements is the stability of the benchmarks. A significant challenge in seafloor geodesy, especially in subduction zones like Cascadia offshore, is the presence of thick sediment covering the seafloor where benchmarks are placed. Additionally, seafloor surveys are costly and have limitations for continuous monitoring of benchmarks. As a result, alternative low-cost geodetic surveys, such as structure-from-motion (SfM), can help address this issue.


As SfM becomes more widely utilized in geoscience, there is a lack of studies specifically focusing on benchmark stability using SfM. Cook & DeSanto (2019) assessed and compared the performance of an ROV-based SfM photo survey with a pressure survey to measure height information. Their results showed agreement between the two methods, with uncertainties at the centimeter scale. Although their 3D photogrammetry model captured the entire scene, including the geodetic benchmark and a pressure recorder attached to a pipe, the model's resolution could be improved using zoom-in video footage recorded by an ROV during more recent surveys.


In this project, I use video footage from the 2023 ROV survey conducted offshore Oregon and Agisoft Metashape to construct a 3D model of the geodetic benchmark (O4) (Cook et al., 2023). This project evaluates the quality of the 3D photogrammetric benchmark model derived using SfM.

## 2. Methods
### 2.1 Benchmark location and structure
The seafloor benchmark O4, situated in deep water at a depth of 620 m, serves as a reference point for 3D photogrammetric modeling. Located at coordinates 44.3666°N, 124.9670°W off the coast of Newport, Oregon, it was deployed from 2014 to 2017 (Fig. 1) (Cook et al., 2023). Its design is based on a model developed initially by Segawa and Fujimoto (1988). The benchmark features a circular base measuring 76.2 cm in diameter and 15 cm in thickness, supported by three 14 cm long legs extending downward. It weighs 145 kg in air and 66.7 kg when submerged in water (Fig. 2) (Cook et al., 2023).
![Seafloor Benchmark Image](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/c0ee8fb9bafabf77f344747fdd42e9bf76551a3b/Figures/Oregon.png)
Figure 1. The map of Oregon offshore and the O4 benchmark (adapted from Cook et al., 2023)



