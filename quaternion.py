import numpy as np

# quaternion = [q_0, q_1, q_2, q_3]
# axis angle = [theta, x, y, z]

def quaternion_to_axis_angle(q):
    if q[3] == 1.0:
        theta = 0.0
        x = 1.0
        y = 0.0
        z = 0.0
        print("Unit quaternion")
        return np.array([x,y,z,theta])    
    
    #print(q[3])
    theta = 2*np.arccos(q[3])
    x = q[0]/np.sin(theta/2)
    y = q[1]/np.sin(theta/2)
    z = q[2]/np.sin(theta/2)
    
    return np.array([x,y,z,theta])  

def axis_angle_to_quaternion(aa):
    q0 = aa[0]*np.sin(aa[3]/2)
    q1 = aa[1]*np.sin(aa[3]/2)
    q2 = aa[2]*np.sin(aa[3]/2)
    q3 = np.cos(aa[3]/2)
    return np.array([q0, q1, q2, q3])

def quat_mul(q_b, q_a):
    q0 = q_a[3]*q_b[0]-q_a[2]*q_b[1]+q_a[1]*q_b[2]+q_a[0]*q_b[3]
    q1 = q_a[2]*q_b[0]+q_a[3]*q_b[1]+q_a[0]*q_b[2]-q_a[1]*q_b[3]
    q2 = -q_a[1]*q_b[0]+q_a[0]*q_b[1]+q_a[3]*q_b[2]+q_a[2]*q_b[3]
    q3 = -q_a[0]*q_b[0]-q_a[1]*q_b[1]-q_a[2]*q_b[2]+q_a[3]*q_b[3]
    return np.array([q0, q1, q2, q3])

def quat_inv(q):
    q0 = -q[0]
    q1 = -q[1]
    q2 = -q[2]
    q3 = q[3]
    return np.array([q0, q1, q2, q3])

def quat_passive_rotation(q, p):
    point = np.array([p[0], p[1], p[2], 0.0])
    return quat_mul(q, quat_mul(point, quat_inv(q)))[0:3]

if __name__ == "__main__":
    point = [10, 0, 0]
    rotation_axis = [0, 1, 0]
    angle = np.pi/2
    
    rotation_quaternion = axis_angle_to_quaternion(np.array([rotation_axis[0], rotation_axis[1], rotation_axis[2], angle]))
    print(quat_passive_rotation(rotation_quaternion, point))
