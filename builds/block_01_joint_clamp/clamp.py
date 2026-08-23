def clamp_one(angle,low,high):
    if angle<low:
        angle = low 
    elif angle>high:
        angle = high 
    
    return angle 


def clamp_all(low,high,*angles):
    clamped_joint_angles = []
    for i in angles:
        if i<low:
            clamped_joint_angles.append(low) 
        elif i>high:
            clamped_joint_angles.append(high)
        else: 
            clamped_joint_angles.append(i) 
    return tuple(clamped_joint_angles)

def clamp_joints(*angles,**limits):
    clamped_joint_angles = {}
    if len(angles)!=len(limits):
        print(f"Mismatch between number of angles and given limits,{"angles" if len(angles)>len(limits) else "joint_limits"} will be discarded")
    for angle_value,limits_key in zip(angles,limits):
        if angle_value<limits[limits_key][0]:
            clamped_joint_angles[limits_key]=limits[limits_key][0]
        elif angle_value > limits[limits_key][1]:
            clamped_joint_angles[limits_key]=limits[limits_key][1]
        else: 
            clamped_joint_angles[limits_key]=angle_value
    return clamped_joint_angles


def report(*angles,**limits):
    clamped_joint_angles = {}
    if len(angles)!=len(limits):
        print(f"Mismatch between number of angles and given limits,{"angles" if len(angles)>len(limits) else "joint_limits"} will be discarded")
    for angle_value,limits_key in zip(angles,limits):
        if angle_value<limits[limits_key][0]:
            print(f"{limits_key:10s} : {float(angle_value):8.1f} -> {float(limits[limits_key][0]):8.1f} CLAMPED")
        elif angle_value > limits[limits_key][1]:
            print(f"{limits_key:10s} : {float(angle_value):8.1f} -> {float(limits[limits_key][1]):8.1f} CLAMPED")
        else: 
            print(f"{limits_key:10s} : {float(angle_value):8.1f} -> {float(angle_value):8.1f} ok")
    return clamped_joint_angles