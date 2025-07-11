import numpy as np

# quaternion = [q_0, q_1, q_2, q_3]
# axis angle = [theta, x, y, z]

def quaternion_to_axis_angle(q):
    if q[0] == 1.0:
        theta = 0.0
        x = 1.0
        y = 0.0
        z = 0.0
        return np.array([theta,x,y,z])    
    theta = 2*np.arccos(q[0])
    x = q[1]/np.sin(theta/2)
    y = q[2]/np.sin(theta/2)
    z = q[3]/np.sin(theta/2)
    return np.array([theta,x,y,z])  

def axis_angle_to_quaternion(aa):
    q0 = np.cos(aa[0]/2)
    q1 = aa[1]*np.sin(aa[0]/2)
    q2 = aa[2]*np.sin(aa[0]/2)
    q3 = aa[3]*np.sin(aa[0]/2)
    return np.array([q0, q1, q2, q3])

def quat_mul(q_a, q_b):
    print()
    q0 = q_a[0]*q_b[0]-q_a[1]*q_b[1]-q_a[2]*q_b[2]-q_a[3]*q_b[3]
    q1 = q_a[0]*q_b[1]-q_a[1]*q_b[0]-q_a[2]*q_b[3]-q_a[3]*q_b[2]
    q2 = q_a[0]*q_b[2]-q_a[1]*q_b[3]-q_a[2]*q_b[0]-q_a[3]*q_b[1]
    q3 = q_a[0]*q_b[3]-q_a[1]*q_b[2]-q_a[2]*q_b[1]-q_a[3]*q_b[0]
    return np.array([q0, q1, q2, q3])

def quat_inv(q):
    q0 = q[0]
    q1 = -q[1]
    q2 = -q[2]
    q3 = -q[3]
    return np.array([q0, q1, q2, q3])

def quat_passive_rotation(q, p):
    point = np.array([0.0 , p[0], p[1], p[2]])
    return quat_mul(q, quat_mul(p, quat_inv(q)))

if __name__ == "__main__":
    point = [10, 0, 0]
    rotation_axis = [0, 1, 1]
    angle = np.pi/2
    
    rotation_quaternion = axis_angle_to_quaternion(np.array([angle, rotation_axis[0], rotation_axis[1], rotation_axis[2]]))
    print(quat_passive_rotation(rotation_quaternion, point))
