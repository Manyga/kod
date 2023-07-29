#py welcome_to_image.py

import os
import cv2
import numpy as np
from varname.helpers import debug
img_path = os.path.abspath('russ.jpg')
debug(img_path)
img = cv2.imread(img_path)
img2draw = img.copy()
img2draw = cv2.resize(img2draw, dsize=None, fx=0.5, fy=0.5)
debug(img.shape)
img_height, img_width, img_channels = img2draw.shape
debug(img_height)
debug(img_width)
img_center_xy = (int(img_width/2), int(img_height/2))
for i in range(20):
    img2draw = cv2.circle(img2draw, center=img_center_xy, radius=int(2*np.e*i), color=(0, 200, 0), thickness=2 )

cv2.imshow('russ', img2draw)
cv2.waitKey(-1) 