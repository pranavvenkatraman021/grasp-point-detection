# imports
import os
import numpy as np
import cv2 
import matplotlib.pyplot as plt

# load the RGB photo of a given object ID
def load_rgb(base_path, pcd_id):
    # opened in BGR order
    img_bgr = cv2.imread(f"{base_path}/pcd{pcd_id}r.png")
    # BGR --> RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb

# load the depth image of a given object ID
def load_depth(base_path, pcd_id):
    # keep raw depth 
    depth = cv2.imread(f"{base_path}/pcd{pcd_id}d.tiff", cv2.IMREAD_UNCHANGED)
    return depth
