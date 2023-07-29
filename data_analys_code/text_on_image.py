mport cv2
import numpy as np

def add_info_to_image(img_path):
    image = cv2.imread(img_path)
    height, width, channels = image.shape
    print(height, width, channels)
    info_field = np.zeros(shape=(int(height/8), width, channels), dtype=image.dtype)
    cv2.putText(
        img=info_field,
        text=img_path,
        org=(20, 40),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=2,
        color=(14,255,200),
        thickness=1
    )
    
    resolution_str = 'Height::{} Width::{} Channels::{}'.format(height, width, channels)
    
    cv2.putText(
        img=info_field,
        text=resolution_str,
        org=(20, 65),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=2,
        color=(15,255,250),
        thickness=1
    )
    
    image_with_info = np.vstack([info_field, image])
    cv2.imshow('result', image_with_info)
    cv2.waitKey(-1)
      
img_path = 'testdata/mem.png'
add_info_to_image(img_path)
