import os 
import cv2
import copy
import numpy as np


def resize_image(img, scale_factor):
    return cv2.resize(img, None, fx=scale_factor, fy=scale_factor)

def chess_desk(img, chess_size_h, chess_size_w):
    height, width, channels = img.shape # Высота , ширина каналы изображения (BGR) в пикселях
    print(img.shape)
    h_step = int(height/chess_size_h)
    w_step = int(width/chess_size_w)
    current_plitochki_count = 0
    current_h = 0
    # idem po colonkam = i
    for i in range(chess_size_h):
        previous_h  = current_h
        current_h += h_step

        current_w = 0
        # idem po strokam = j
        for j in range(chess_size_w):
            previous_w  = current_w
            current_w += w_step
            # print('H: {}:{}  W: {}:{}'.format(
            #     previous_h, 
            #     current_h, 
            #     previous_w, 
            #     current_w
            # ))
            crop = img[previous_h:current_h,previous_w:current_w,:]
            # if j%2 == 0:
            #     if j != 0:
            #         crop *= 0 

            if i%2 == 0:
                 
                if current_plitochki_count %2 == 0:
                    crop *= 0
            else:
                if current_plitochki_count %2 != 0:
                    crop *= 0
            current_plitochki_count += 1                    
            # cv2.imshow('crop', crop.astype(np.uint8))
            # cv2.waitKey(-1)

    cv2.imwrite('out/chess_desk.png', img)

    
    # cv2.imshow('chess_desk', img)
    # cv2.waitKey(-1)
    
    
    
    
    # for i in range(1000):
    #     # temp_img = copy.copy(img)
    #     # temp_img = cv2.putText(temp_img, str(i), (20,200), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0))
    #     cv2.imshow('chess', temp_img)
    #     cv2.waitKey(60)
    #     cv2.destroyAllWindows()