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

![Blueprint](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%202.png)
Figure 2. The benchmark structure (from Applied Physics Laboratory, University of Washington)

### 2.2 Photogrammetry survey
#### 2.2.1 Data preparation and software
The video footage used for this study was obtained during a benchmark survey conducted in July 2023. The scene was recorded with a Sulis Z70 camera, an underwater device specifically designed for ROV deployment and capable of capturing 4K Ultra HD video. Screenshots from the footage, each with a resolution of approximately 7 MB, were used as inputs for the Structure-from-Motion (SfM) process. A total of 63 images were selected as suitable candidates for modeling. Prior to SfM processing, the raw images underwent preprocessing to adjust contrast, brightness, and color channels, following the steps outlined in `Image_processing.py`. (accessed via https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM)

The differences between the raw and processed images are illustrated in Fig. 3. The 3D model of the O4 seafloor benchmark was constructed using Agisoft Metashape Professional, a photogrammetric software widely adopted in geoscience applications (e.g., Over et al., 2021).
![Benchmark](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%203.png)
Figure 3. (left) The raw screenshot of the video footage. (right) The processed image using `Image_processing.py`

#### 2.2.2 Workflow in constructing a 3D model using Agisoft Metashape
1) Add Photos
   - The first step is to add preprocessed photos in Agisoft.
     
2) Align Photos
   - Align Photos is a process using the Scale-Invariant Feature Transform (SIFT) algorithm to identify common features in all the photos. The setting is shown in Fig. 4.
   - It returns a rough guess for the position and orientation of the cameras and point cloud of a 3D model (Fig. 5). Fig. 10 shows the result excluding the camera positions.
   - It is crucial to delete point clouds that are outliers, potentially from noise and background.
   - 13 Makers are added to align each photo further (Fig. 6).
   - Some markers (makers 12 and 13) will be selected for scaling and setting coordinates.
![align photo](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%204.png)
Figure 4. The setting of Align Photos

![cloud point w/ cameras](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%205.png)
Figure 5. Point cloud with cameras

![makers](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%206.png)
Figure 6. Photos used to construct the model with 13 markers, represented by green flags

3) Build Dense Cloud
   - The most time-consuming step is constructing a dense cloud by constructing depth maps for every pixel in the overlapping images (Fig. 11). It’s then used for building a mesh. The setting is shown in Fig. 7.
   - The depth filtering setting controls how the software handles noise and unwanted points when generating a dense point cloud. This setting applies minimal filtering, keeping most of the points.
![build dense cloud](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%207.png)
Figure 7. The setting of Build Dense Cloud

4) Build Mesh
   - This step in the Workflow constructs a 3D surface or a mesh from the depth maps or dense point cloud from the previous step. The mesh is made up of polygons that define the model’s geometric structure. The setting is shown in Fig. 8.
![build mesh](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%208.png)
Figure 8. The setting of Build Mesh

5) Build Texture
   - This process generates a photo-realistic surface representation of the 3D SfM model by projecting image data–details and colors–from the aligned photos onto the model’s mesh (Fig. 12). The setting is shown in Fig. 9.
![build texture](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%209.png)
Figure 9. The setting of Build Mesh

## 3. Results
![point cloud](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%2010.png)
Figure 10. Point Cloud displays the draft of the 3D model, including outliers from background and noise.
![dense cloud](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%2011.png)
Figure 11. Dense Cloud shows the high resolution of the three models by constructing depth maps with fewer outlier points. The plate above the pole disappeared during this process.
![model texture](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%2012.png)
Figure 12. Model textured combines information from mesh and aligned images to construct realistic 3D models. Outlier points are removed.

## 4. Discussion
The plate above the pole is missing in the Dense Cloud (Fig. 11), unlike the Point Cloud (Fig. 10). This missing part of the 3D model likely results from misinterpretation by Agisoft Metashape.

First, the plate may be treated as a floating object due to insufficient tie points connecting it to the pole. Few images capture the connection between the plate and the pole, likely because it is challenging to position the camera to simultaneously center both the benchmark and the pole within the frame (Fig. 13). Additionally, the ROV recorded video footage of the benchmark from only one angle, limiting the number of useful images showing the connection between the plate and pole. A potential solution is to record video footage from multiple angles and altitudes to better capture details of the connection.

Second, the plate's thinness and lack of texture present challenges for depth map construction. These characteristics can lead to unreliable depth information. Even with mild depth filtering applied, points that appeared to connect the plate and pole might have been removed, as they were potentially interpreted as noise (Fig. 14).

![point cloud w/markers](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%2013.png)
Figure 13. Point Cloud with makers and scale bar. The tie points of the plate are still present, but the plate is too thin, and a few tie points connect the plate and the pole.
![model textured w/markers](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%2014.png)
Figure 14. Model Textured with markers and scale bar. The plate is removed after the Dense Cloud process while the markers are still present.
![working window](https://github.com/Benz-Poobua/3D-model-seafloor-benchmark-by-SfM/blob/93430622894041f301846efd07422a354e364b58/Figures/Fig.%2015.png)
Figure 15. Agisoft Metashape working window. We select points 12 and 13 to construct a scale bar and scaling reference. The coordinates (X, Y, Z) are estimated based on the reference. Accuracy values are default values. The exaggerated sizes of other marks suggest unreliable scales due to the lack of comprehensive scales of either the benchmark or the pole.


The model size is not absolute, so Agisoft Metashape requires known-size objects as references for scaling. The geometry of the benchmark and pole, as provided in the blueprint (Fig. 2) and described by Cook & DeSanto (2019), can be used for this purpose. The benchmark's diameter and the plate's dimensions can serve as references for horizontal scaling. However, placing markers to measure the diameter is highly challenging due to the lack of distinct points to anchor while rotating the camera.

Vertical scaling can be inferred from the benchmark’s height, but the plate’s thickness remains unknown. Consequently, we have reliable information for only one scale (either horizontal or vertical) for both known-size objects. This limitation results in a highly inaccurate estimated scale for the model (Fig. 15).

## 5. Conclusion
Using zoomed-in video footage recorded by a Sulis Z70 camera controlled by an ROV, it is possible to construct a high-resolution 3D photogrammetric model of a geodetic benchmark on the seafloor. The distortion in the video is negligible, and image processing can be efficiently applied using Python on photosets with consistent lighting. The lighting and color tones in the scenes are generally uniform, provided that seafloor dust or sediments are absent. Despite capturing fine details of the benchmark model, missing parts occur due to the limited video shooting angles and the challenge of centering the pole in the frame while controlling the ROV. Additionally, difficulties in scaling arise from the inability to place markers to measure the benchmark's diameter or the plate’s geometry (e.g., thickness).

A potential solution is to capture video footage from multiple angles, ensuring more scenes that highlight the connection between the plate and the pole. The scaling challenge can be addressed by adding distinct, visible markers on the benchmark to indicate its diameter for horizontal scaling. The vertical scale can be determined using an object affixed to the benchmark that remains above the seafloor, preventing submergence by sediments.

By resolving these issues, it will be possible to compare the point cloud of the benchmark across different surveys. This approach can help infer surface deformation and assess benchmark stability using cost-effective survey methods.

## Dataset
The files can be accessed via https://drive.google.com/file/d/1Ud76AJ6otNhwDPRVwFe4qcs7OEPZ7gLn/view?usp=sharing
## References
Ballu, V., Bonnefond, P., Calmant, S., Bouin, M. N., Pelletier, B., Laurain, O., ... & De Viron, O. (2013). Using altimetry and seafloor pressure data to estimate vertical deformation offshore: Vanuatu case study. Advances in Space Research, 51(8), 1335-1351.

Bürgmann, R., & Chadwell, D. (2014). Seafloor geodesy. Annual Review of Earth and Planetary Sciences, 42(1), 509-534.

Cook, M. J., & DeSanto, J. B. (2019). Validation of Geodetic Seafloor Benchmark Stability Using Structure‐From‐Motion and Seafloor Pressure Data. Earth and Space Science, 6(9), 1781-1786.

Cook, M. J., Fredrickson, E. K., Roland, E. C., Sasagawa, G. S., Schmidt, D. A., Wilcock, W. S., & Zumberge, M. A. (2023). Calibrated absolute seafloor pressure measurements for geodesy in Cascadia. Journal of Geophysical Research: Solid Earth, 128(6), e2023JB026413.

David, C. G., Kohl, N., Casella, E., Rovere, A., Ballesteros, P., & Schlurmann, T. (2021). Structure-from-Motion on shallow reefs and beaches: potential and limitations of consumer-grade drones to reconstruct topography and bathymetry. Coral Reefs, 40(3), 835-851.

Lowe, G. (2004). Sift-the scale invariant feature transform. Int. J, 2(91-110), 2.

Over, J. S. R., Ritchie, A. C., Kranenburg, C. J., Brown, J. A., Buscombe, D. D., Noble, T., ... & Wernette, P. A. (2021). Processing coastal imagery with Agisoft Metashape Professional Edition, version 1.6—Structure from motion workflow documentation (No. 2021-1039). US Geological Survey.

Polster, A., Fabian, M., & Villinger, H. (2009). Effective resolution and drift of Paroscientific pressure sensors derived from long‐term seafloor measurements. Geochemistry, Geophysics, Geosystems, 10(8).

Schonberger, J. L., & Frahm, J. M. (2016). Structure-from-motion revisited. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 4104-4113).

Segawa, J., & Fujimoto, H. (1988). Observation of an ocean bottom station installed in the Sagami Bay and replacement of the acoustic tran- sponder attached to it. Deep Sea Research, 256, 251–257. Japan Agency for Marine-Earth Science and Technology.

Snavely, N., Seitz, S. M., & Szeliski, R. (2006). Photo tourism: exploring photo collections in 3D. In ACM siggraph 2006 papers (pp. 835-846).

Snavely, N., Seitz, S. M., & Szeliski, R. (2008). Modeling the world from internet photo collections. International journal of computer vision, 80, 189-210.

Storlazzi, C. D., Dartnell, P., Hatcher, G. A., & Gibbs, A. E. (2016). End of the chain? Rugosity and fine-scale bathymetry from existing underwater digital imagery using structure-from-motion (SfM) technology. Coral Reefs, 35(3), 889-894.

Westoby, M. J., Brasington, J., Glasser, N. F., Hambrey, M. J., & Reynolds, J. M. (2012). ‘Structure-from-Motion’photogrammetry: A low-cost, effective tool for geoscience applications. Geomorphology, 179, 300-314.

