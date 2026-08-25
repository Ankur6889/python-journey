def clamp_one(angle,low,high):
    if angle<low:
        angle = low 
    elif angle>high:
        angle = high 
    
    return angle 


def clamp_all(low,high,*angles):
    clamped_joint_angles = []
    for i in angles:
        clamped_joint_angles.append(clamp_one(i,low,high))
    return tuple(clamped_joint_angles)

def clamp_joints(*angles,**limits):
    clamped_joint_angles = {}
    if len(angles)!=len(limits):
        print(f"Mismatch between number of angles and given limits,{"angles" if len(angles)>len(limits) else "joint_limits"} will be discarded")
    for angle_value,limits_key in zip(angles,limits):
        clamped_joint_angles[limits_key]=clamp_one(angle_value,limits[limits_key][0],limits[limits_key][1])
    return clamped_joint_angles


def report(*angles,**limits):
    clamped_joint_angles = {}
    if len(angles)!=len(limits):
        print(f"Mismatch between number of angles and given limits,{"angles" if len(angles)>len(limits) else "joint_limits"} will be discarded")
    for angle_value,limits_key in zip(angles,limits):
        safe = clamp_one(angle_value,limits[limits_key][0],limits[limits_key][1])
        clamped_joint_angles[limits_key]=safe
        print(f"{limits_key:10s} : {angle_value:8.1f} -> {safe:8.1f} {"CLAMPED" if safe!=angle_value else "ok"}")
    return clamped_joint_angles