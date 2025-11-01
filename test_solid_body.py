import solid_body
import quaternion
import numpy as np

q_init = quaternion.axis_angle_to_quaternion(np.array([1.0, 0.0, 0.0, 0.0]))
omega_init = np.array([1.0, 1.0, 0.0])
pos_init = np.array([0.0, 0.0, 0.0])
vel_init = np.array([0.0, 0.0, 0.0])
sb = solid_body.solid_body(q_init=q_init, omega_init=omega_init, pos_init=pos_init, vel_init=vel_init)
for i in range(1000):
    sb.integration_step(0.001)
    #print("----------------------------------------------------------------------------")
    print(f"Axis angle: {quaternion.quaternion_to_axis_angle(sb.orientation_quaternion_I)}")
    #print(f"Quaternion: {sb.orientation_quaternion_I}")
    #print(f"Orientation quaternion norm: {np.linalg.norm(sb.orientation_quaternion_I)}")