import cv2
import numpy as np
import limits as lm
import masks
import reactions as r


finish = False

def detect(drone, img, recorder, SHOW, minsizeObject=200):
    global finish

    objects = shape_recognition(img, SHOW, minsizeObject)    
    _, red, green, blue, yellow = color_recognition(img)

    #                                           < -------------  add: after object has been detected, remove it from detectable objects

    if True in objects:

        if (objects[2] and yellow) or finish:    
            r.react_yellowcircle(drone, img)    
            finish = True 

            return finish 

            # return True         <------ if other shapes added, to be removed


    # return False                  <------ if other shapes added, to be removed



    #         return object_spotted
    #     elif objects[0] and red:
    #         r.react_redrectangle(recorder)

    #     elif objects[0] and blue:
    #         r.react_bluerectangle(recorder)

    #     elif objects[1] and red:
    #         r.react_redtriangle(drone)

    #     elif objects[1] and blue:
    #         r.react_bluetriangle(drone)

    #     elif objects[2] and red:
    #         r.react_redcircle(drone)

    #     elif objects[2] and blue:
    #         r.react_bluecircle(drone)



    #     elif objects[2] and green:               #     <------------------------
    #         object_spotted = True

    #         return object_spotted





    #     else:
    #         print("unknown colour for detected object")




    








def shape_recognition(img, SHOW, minsizeObject=200):
    global approx, right_angles

    # resize
    # img = cv2.resize(img, (480, 360))

    # crop
    img = img[0:int(img.shape[0]-img.shape[0]*0.15), 60:img.shape[1]-60]

    # blurring to get rid off noise
    blurred = cv2.GaussianBlur(img, (5,5), 0)

    # sharpening (effective) #
    kernel = np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])


    img = cv2.filter2D(blurred, -1, kernel)


    threshed_img, _, _, _, _ = color_recognition(img)
    threshed_img = cv2.bitwise_not(threshed_img)



    contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 

    
    Rectangle = False
    Triangle = False
    Circle = False
    
    objects = [Rectangle, Triangle, Circle]


    for i, contour in enumerate(contours):
        if i == 0:
            pass

        else:
            if cv2.contourArea(contour) > minsizeObject:
                epsilon = 0.02*cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)


                x, y, w, h= cv2.boundingRect(approx)

                # box
                start_point = (int(x-7), int(y-7))
                end_point = (int(x+w+7), int(y+h+7))
                thickness_rect = 1

                # text
                x1, y1 = int(end_point[0]-50), int(end_point[1]+15)
                org = (x1, y1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                colour = (66,163,31)
                font_scale = 0.5  
                thickness = 2  




                ####   angles (effective)                    
                right_angles = []
                anglesT = []
                anglesR = []

                if len(approx) >= 3:
                    anglesT = [get_angle(approx[i - 1][0], approx[i][0], approx[(i + 1) % 3][0]) for i in range(3)]

                if len(approx) >= 4:
                    anglesR = [np.degrees(np.arctan2(approx[i - 1][0][1] - approx[i][0][1], approx[i - 1][0][0] - approx[i][0][0])) for i in range(4)]
                    right_angles = [angle for angle in anglesR if 80 < angle < 100 or -100 < angle < -80]
                #####






                                        # <-----  3->4
                if len(approx) == 4 or len(right_angles) == 4:
                    if SHOW:
                        cv2.rectangle(img, start_point, end_point, colour, thickness_rect)
                        cv2.putText(img, "Rectangle", org, font, font_scale, colour, thickness)
                    objects[0] = True


                elif len(approx) == 3 or all(angle > 55 and angle < 70 for angle in anglesT):  
                    if SHOW:
                        cv2.rectangle(img, start_point, end_point, colour, thickness_rect)          
                        cv2.putText(img, "Triangle", org, font, font_scale, colour, thickness)
                    objects[1] = True


                else:
                    if SHOW:
                        cv2.rectangle(img, start_point, end_point, colour, thickness_rect)
                        cv2.putText(img, "Circle", org, font, font_scale, colour, thickness)
                    objects[2] = True
    

    if SHOW:
        # cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
        cv2.imshow('Result', img)
        cv2.waitKey(1)



    return objects






def get_angle(p1, p2, p3):
    v1 = p1 - p2
    v2 = p3 - p2
    angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    return np.degrees(angle)






def color_recognition(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_R = masks.get_red_mask(hsv_frame)
    mask_G = masks.get_green_mask(hsv_frame)
    mask_B = masks.get_blue_mask(hsv_frame)
    mask_Y = masks.get_yellow_mask(hsv_frame)


    # comment out, create a function for each colour
    mask = mask_R + mask_G + mask_B + mask_Y

    # cv2.imshow("img", frame)
    # cv2.imshow("red", mask_R)
    # cv2.imshow("Green", mask_G)
    # cv2.imshow("Blue", mask_B)
    # cv2.imshow("Yellow", mask_Y)
    # cv2.waitKey(1)      

    red, green, blue, yellow = False, False, False, False

    if ((np.sum(mask_R == 255) // mask_R.size)*100) >= 10:
        red = True

    if ((np.sum(mask_G == 255) // mask_G.size)*100) >= 10:
        green = True

    if ((np.sum(mask_B == 255) // mask_B.size)*100) >= 10:
        blue = True

    if ((np.sum(mask_Y == 255) // mask_Y.size)*100) >= 10:
        yellow = True

    return mask, red, green, blue, yellow
    












### LIMITS TESTING
# frame = cv2.imread("img\\krchova ucebna.jpeg")
# frame000 = cv2.imread("img\\farby tvarov.jpg")
# frame000 = cv2.resize(frame000,(500,600))
# frame1 = cv2.imread("img\\krchova ucebna2.jpeg")
# frame2 = cv2.imread("img\\krchova ucebna3.jpeg")
# frame3 = cv2.imread("img\\laminat.jpg")
# frame4 = cv2.imread("img\\laminat2.jpg")
# frame5 = cv2.imread("img\\parkrtyidk.jpeg")
# frame6 = cv2.imread("img\\stare parkery .png")
# frame7 = cv2.imread("img\\stare parkety.jpg")
# frame8 = cv2.imread("img\\parkety-vzor-stromecek.jpg")


# # 
# color_recognition(frame000)
# color_recognition(frame2)
# color_recognition(frame3)
# color_recognition(frame4)
# color_recognition(frame5)
# color_recognition(frame6)
# color_recognition(frame7)
# color_recognition(frame8)