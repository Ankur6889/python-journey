print("robot.py is running")

MAX_ANGLE = 180


def clamp(angle):
    if angle > MAX_ANGLE:
        return MAX_ANGLE
    return angle
