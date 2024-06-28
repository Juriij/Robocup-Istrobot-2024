import cv2


def get_frame(drone, width=360, height=240):
    img = drone.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (width, height))
    return img