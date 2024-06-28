import cv2
import numpy as np
import time



def follow(drone, img, SHOW):
    active_regions = region_activity(img, SHOW)
     


    lr, fb, ud, yaw = 0, 0, 0, 0


    if len(active_regions) == 1:
        if active_regions == [1]:
            lr = -10
            drone.send_rc_control(lr, fb, ud, yaw)  # go left

        elif active_regions == [2]:
            lr = -10
            drone.send_rc_control(lr, fb, ud, yaw)  # go slight left

        elif active_regions == [3]:
            fb = 10
            drone.send_rc_control(lr, fb, ud, yaw)  # go forward

        elif active_regions == [4]:
            lr = 10
            drone.send_rc_control(lr, fb, ud, yaw)  # go slight right

        elif active_regions == [5]:
            lr = 10
            drone.send_rc_control(lr, fb, ud, yaw)  # go right


    elif len(active_regions) == 2:
        if active_regions == [2,3]:
            fb = 10
            yaw = -20
            drone.send_rc_control(lr, fb, ud, yaw)  # slight curve left

        elif active_regions == [3,4]:
            fb = 10
            yaw = 20
            drone.send_rc_control(lr, fb, ud, yaw)  # slight curve right 

        # elif active_regions == [1,2]:
        #     pass  # stop and rotate left 90 degrees

        # elif active_regions == [4,5]:
        #     pass  # stop and rotate right 90 degrees


    elif len(active_regions) == 3:
        if active_regions == [1,2,3]:
            fb = 8
            yaw = -40
            drone.send_rc_control(lr, fb, ud, yaw)  # curve left (slow down)

        elif active_regions == [3,4,5]:
            fb = 8
            yaw = 40
            drone.send_rc_control(lr, fb, ud, yaw)  # curve right (slow down) 

        elif active_regions == [2,3,4]:  # special case, when the drone is to flying too low
            pass  # go forward 


    elif len(active_regions) == 4:
        print("four regions")

    elif len(active_regions) == 5:
        print("five regions")


    print(lr, fb, ud, yaw)








def region_activity(img, SHOW):
    # cv2.imshow("original", img)
    # cv2.waitKey(1)
    img = img[:img.shape[0]-50, 90:img.shape[1]-90]
    # cv2.imshow("cropped", img)
    # cv2.waitKey(1)
    img = thresholding(img)  


    active_regions = []
    for i in range(1,6):
        img_portion = img[0:img.shape[0], (img.shape[1]*(i-1))//5:(img.shape[1]*i)//5]

        if int((((np.sum(img_portion == 0)) / (img_portion.size))*100)) >= 5:     
            active_regions.append(i) 
                                                                                    # IDEA: responsive detectivness of black in relation with an altitude





    if SHOW:
        for i in range(1,5):
            cv2.line(img, ((img.shape[1]*i)//5, 0), ((img.shape[1]*i)//5, img.shape[0]), (180), 1)

        cv2.imshow("camera", img)
        cv2.waitKey(1)
        # print(active_regions)

    return active_regions




    


def thresholding(img, thresh=70):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _ , img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    return img