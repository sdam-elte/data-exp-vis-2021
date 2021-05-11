# Visualize a pointcloud with pptk and open3d
# Sample data can be downloaded from https://drive.google.com/file/d/1DUEy-gayYudkuJUou_cfNmPAmwdbbgml/view?usp=sharing

# Tutorial: https://towardsdatascience.com/guide-to-real-time-visualisation-of-massive-3d-point-clouds-in-python-ea6f00241ee0

import numpy as np
import laspy as lp
import open3d as o3d
import pptk

input_path="./"
dataname="2020_Drone_M"
point_cloud=lp.file.File(input_path+dataname+".las", mode="r")
points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()

factor=10
decimated_points_random = points[::factor]

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors/65535)
#pcd.normals = o3d.utility.Vector3dVector(normals)
o3d.visualization.draw_geometries([pcd])
