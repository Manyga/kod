import os
import numpy as np
import cv2

img_path = os.path.abspath('russ.jpg')
print(img_path)
img = cv2.imread(img_path)
print(img.shape)