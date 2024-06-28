from djitellopy import tello
import camera_access as camera
import cv2 
from threading import Thread
import time
import masks


# from KeyboardControl import getKeyboardInput
# from KeyPress import init
# init()
import line_following as line
import object_recognition as object
import reactions as r

drone = tello.Tello()
drone.connect()
drone.streamon()

recorder = Thread(target=r.videoRecorder)
Running = True
takeoff = True

while Running:
    img = camera.get_frame(drone)
    r.get_img(img)

    img = cv2.flip(img, 0)        #  mirror         -> on
                                  #  without mirror -> off 

    # r.react_yellowcircle(drone, img)

    finish = object.detect(drone, img, recorder, False, 200)

    if not finish:
        line.follow(drone, img, True)



    if takeoff:
        drone.takeoff()
        takeoff = False
 




    # linefollow_off = object.detect(drone, img, recorder, False, 200)       <------ if other shapes added, to be removed


    # if not linefollow_off:                                                 <------ if other shapes added, to be removed
    #    line.follow(drone, img, True)


    # TESTING #

    # movement = getKeyboardInput(drone, 20)
    # drone.send_rc_control(movement[0], movement[1], movement[2], movement[3]) 

    ###########