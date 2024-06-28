import KeyPress as kp



def getKeyboardInput(drone, velocity=50):

    """
    Returns velocity values relatively to keyboard input for left-right, forward-back, up-down, yaw .
    'e' is takeoff and 'q' is land command
    """
    

    lr, fb, ud, yv = 0, 0, 0, 0
                                         # movement
    
    
    if kp.isPressed("RIGHT"):
        lr = velocity
    elif kp.isPressed("LEFT"):
        lr = -velocity

    if kp.isPressed("UP"):
        fb = velocity
    elif kp.isPressed("DOWN"):
        fb = -velocity

    if kp.isPressed("w"):
        ud = velocity
    elif kp.isPressed("s"):
        ud = -velocity

    if kp.isPressed("d"):
        yv = velocity
    elif kp.isPressed("a"):
        yv = -velocity

                                        # takeoff, land
    if kp.isPressed("q"):
        drone.land()

    if kp.isPressed("e"):
        drone.takeoff()



    return [lr, fb, ud, yv]