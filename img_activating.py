import os
import cv2


from tools_folder import tools

if __name__ == '__main__':
    path = 'testdata\jeezus.jpg'
    image = cv2.imread(path)
    # resized_image = tools.resize_image(image, 0.7)
    chess_desk_size_h = 8
    chess_desk_size_w = 8
    tools.chess_desk(image, chess_desk_size_h, chess_desk_size_w)
    