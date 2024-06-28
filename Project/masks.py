import numpy as np
import cv2
import limits as lm

def get_red_mask(hsv_frame):
    upper_limit_R1, upper_limit_R2, lower_limit_R1, lower_limit_R2 = lm.get_limits_red()
    mask_red_1 = cv2.inRange(hsv_frame, lower_limit_R1, upper_limit_R1)
    mask_red_2 = cv2.inRange(hsv_frame, lower_limit_R2, upper_limit_R2)
    mask_R = mask_red_1 + mask_red_2

    return mask_R



def get_green_mask(hsv_frame):
    upper_limit_G, lower_limit_G = lm.get_limits_green() 
    mask_G = cv2.inRange(hsv_frame, lower_limit_G, upper_limit_G)

    return mask_G



def get_blue_mask(hsv_frame):
    upper_limit_B, lower_limit_B = lm.get_limits_blue()
    mask_B = cv2.inRange(hsv_frame, lower_limit_B, upper_limit_B)

    return mask_B



def get_yellow_mask(hsv_frame):
    upper_limit_Y, lower_limit_Y = lm.get_limits_yellow()
    mask_Y = cv2.inRange(hsv_frame, lower_limit_Y, upper_limit_Y)

    return mask_Y