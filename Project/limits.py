import numpy as np
import cv2


def get_limits_red():
    sample = np.uint8([[[0,0,255]]])
    hsv_sample = cv2.cvtColor(sample, cv2.COLOR_RGB2HLS_FULL)

    lower_limit = hsv_sample[0][0][0] - 170, 80, 80       
    upper_limit = hsv_sample[0][0][0] - 165, 255, 255    
    lower_limit1 = hsv_sample[0][0][0] - 10, 80, 80
    upper_limit1 = hsv_sample[0][0][0] + 20, 255, 255 

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)
    lower_limit1 = np.array(lower_limit1, dtype=np.uint8)
    upper_limit1 = np.array(upper_limit1, dtype=np.uint8)

    return upper_limit, upper_limit1, lower_limit, lower_limit1


def get_limits_green():
    sample = np.uint8([[[0,255,0]]])
    hsv_sample = cv2.cvtColor(sample, cv2.COLOR_RGB2HLS_FULL)

    lower_limit = hsv_sample[0][0][0] - 20, 50, 50
    upper_limit = hsv_sample[0][0][0] + 13, 255, 255   

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return upper_limit, lower_limit


def get_limits_blue():
    sample = np.uint8([[[255,0,0]]])
    hsv_sample = cv2.cvtColor(sample, cv2.COLOR_RGB2HLS_FULL)

    lower_limit = hsv_sample[0][0][0] + 80, 80, 80       
    upper_limit = hsv_sample[0][0][0] - 130, 255, 255   

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return upper_limit, lower_limit


def get_limits_yellow():
    sample = np.uint8([[[255,255,0]]])
    hsv_sample = cv2.cvtColor(sample, cv2.COLOR_RGB2HLS_FULL)

    lower_limit = hsv_sample[0][0][0] - 19, 80, 80      
    upper_limit = hsv_sample[0][0][0] + 5, 255, 255  

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return upper_limit, lower_limit