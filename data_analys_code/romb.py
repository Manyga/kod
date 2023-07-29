import cv2
import os
import numpy as np

image_path = 'meme.PNG'
image = cv2.imread(image_path)
print(image.shape)
imgtodraw = image.copy()
imgtodraw = cv2.resize(
    imgtodraw, 
    dsize=None,
    fx=0.5,
    fy=0.5
)
#imgtodraw= cv2.rectangle(imgtodraw, pt1=(100,100), pt2=(200,200), color=(255,0,0),thickness=7)
#cv2.imshow('ploho',imgtodraw)
#cv2.waitKey(-1)
image_height, image_width, image_channels = imgtodraw.shape
pt1_top_left_xy = (15,35) 
pt2_bot_right_xy = (450,400)

def draw_romb(imgtodraw, top_left_xy, bot_right_xy):
    imgtodraw= cv2.rectangle(imgtodraw, pt1=top_left_xy, pt2=bot_right_xy, color=(255,0,0),thickness=7)
    bbox_height = abs(bot_right_xy[1] - top_left_xy[1])
    bbox_width = abs(bot_right_xy[0] - top_left_xy[0])
    top_middle_xy = (
        int(bot_right_xy[0] - bbox_width/2),
        top_left_xy[1]
    )
    bot_middle_xy = (
        int(bot_right_xy[0] - bbox_width/2),
        bot_right_xy[1]
    )
    left_middle_xy = (
        top_left_xy[0],
        int(bot_right_xy[1] - bbox_height/2)
    )
    right_middle_xy = (
        bot_right_xy[0],
        int(bot_right_xy[1] - bbox_height/2)
    )
    vertex = [left_middle_xy, top_middle_xy, right_middle_xy, bot_middle_xy]
    for i in range(len(vertex)):
        point_1_id = i
        point_2_id = i+1
        if i == len(vertex)-1:
            point_2_id = 0 
        cv2.line(
            img=imgtodraw,
            pt1=vertex[point_1_id],
            pt2=vertex[point_2_id],
            color=(0,255,0),
            thickness=5
        )
   
    for point in vertex:
        imgtodraw=cv2.circle(
            imgtodraw, 
            center=point, 
            radius=2, 
            color=(255, 255, 0), 
            thickness=2
        )

    cv2.imshow('ploho',imgtodraw)
    cv2.waitKey(-1)

draw_romb(
    imgtodraw=imgtodraw,
    top_left_xy=pt1_top_left_xy,
    bot_right_xy=pt2_bot_right_xy
)
