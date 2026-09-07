from arm.limits import MAX_ANGLE

def clamp(angle):
    if angle > MAX_ANGLE:
        return MAX_ANGLE
    return angle
