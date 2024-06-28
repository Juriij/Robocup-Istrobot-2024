import numpy as np
import cv2
import limits as lm
import masks

def color_recognition(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_R = masks.get_red_mask(hsv_frame)
    mask_G = masks.get_green_mask(hsv_frame)
    mask_B = masks.get_blue_mask(hsv_frame)
    mask_Y = masks.get_yellow_mask(hsv_frame)


    #zakomentovat, spravit malu funkciu pre kazdu farbus
    mask = mask_R + mask_G + mask_B + mask_Y

    cv2.imshow("red", mask_R)
    cv2.imshow("Green", mask_G)
    cv2.imshow("Blue", mask_B)
    cv2.imshow("Yellow", mask_Y)
    cv2.waitKey(1)

    return mask
