import time
import cv2
import numpy as np
import masks


def get_img(IMAGE):
    global img
    img = IMAGE


def videoRecorder():
    global keepRecording, img


    height, width, _ = img.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(img)
        time.sleep(1 / 30)

    video.release()




def split_image(image):
    height, width = image.shape[:2]

    top_left = image[:height//2, :width//2]
    top_right = image[:height//2, width//2:]
    bottom_left = image[height//2:, :width//2]
    bottom_right = image[height//2:, width//2:]

    return top_left, top_right, bottom_left, bottom_right



def react_redrectangle(recorder):
    global keepRecording

    keepRecording = True
    recorder.start()


def react_bluerectangle(recorder):
    global keepRecording
  
    keepRecording = False
    recorder.join()


def react_redtriangle(drone):
    drone.rotate_counter_clockwise(360)


def react_bluetriangle(drone):
    drone.rotate_clockwise(360)

def react_yellowcircle(drone, img):
    hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    threshed = masks.get_yellow_mask(hsv_frame)

    top_left, top_right, bottom_left, bottom_right = split_image(threshed)

    cv2.imshow("top_left", top_left)
    cv2.imshow("top_right", top_right)
    cv2.imshow("bottom_left", bottom_left)
    cv2.imshow("bottom_right", bottom_right)
    cv2.waitKey(1)