#py welcome_to_image.py

import os
import cv2
import numpy as np

img_path = os.path.abspath('russ.jpg')
print(img_path)
img = cv2.imread(img_path)
print(img.shape)
img_height, img_width, img_channels = img.shape
print(img_height)
print(img_width)
img_top = img[:100, :, :]
out_path = 'top_russ.jpg'
cv2.imwrite(out_path, img_top)
print('written to', os.path.abspath(out_path))
img_left = img[:, 200:400, :]
out_path = 'left_russ.jpg'
cv2.imwrite(out_path, img_left)
print('written to', os.path.abspath(out_path))
img_centre = img[350:450,250:450, :]
out_path = 'centre_russ.jpg'
cv2.imwrite(out_path, img_centre)
print('written to', os.path.abspath(out_path))

#pupok = img_centre.copy()
#pupok = cv2.resize(pupok, dsize = None, fx = 2.0,fy = 2.0 )
#print(pupok.shape)
#pupok[:, :, 0] = 255 #зануляем синий канал
#pupok[:, :, 2] *= 0 #зануляем красный канал
#print(pupok)
#cv2.imshow('russ', pupok)
#cv2.waitKey(-1)

w_divider = 12
x_step = int(img_width/ w_divider)
current_x = 0
for i in range(w_divider):
    previous_x = current_x
    current_x += x_step
    if i%2 == 0:
        continue
    print(current_x)
    crop = img[
        :,
        previous_x:current_x,
        :
    ] 
    crop *= 0 #посмотреть видео мл вебм  10 минута
    current_x += x_step
cv2.imshow('russ', img)
cv2.waitKey(-1)    