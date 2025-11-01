import solid_body
import quaternion
import numpy as np
import matplotlib.pyplot as plt

q_init = quaternion.axis_angle_to_quaternion(np.array([0.0, 1.0, 0.0, 0.0]))
omega_init = np.array([1.0, 1.0, 0.0])
pos_init = np.array([0.0, 0.0, 0.0])
vel_init = np.array([0.0, 0.0, 0.0])
sb = solid_body.solid_body(q_init=q_init, omega_init=omega_init, pos_init=pos_init, vel_init=vel_init)
orientation_history = []
for i in range(1000):
    orientation_history.append(np.copy(sb.orientation_quaternion_I))
    sb.integration_step(0.01)
    #print("----------------------------------------------------------------------------")
    #print(f"Axis angle: {quaternion.quaternion_to_axis_angle(sb.orientation_quaternion_I)}")
    #print(f"Quaternion: {sb.orientation_quaternion_I}")
    #print(f"Orientation quaternion norm: {np.linalg.norm(sb.orientation_quaternion_I)}")

# plotting
orientation_history_euler_parameters = []
for q in orientation_history:
    orientation_history_euler_parameters.append(quaternion.quaternion_to_axis_angle(q).tolist())
    #print(q)

orientation_history_euler_parameters = np.array(orientation_history_euler_parameters)
#print(orientation_history_euler_parameters)
#print(orientation_history_euler_parameters.T[3])

fig, axs = plt.subplots(2)
axs[0].plot(orientation_history_euler_parameters.T[0])
axs[0].plot(orientation_history_euler_parameters.T[1])
axs[0].plot(orientation_history_euler_parameters.T[2])
axs[1].plot(orientation_history_euler_parameters.T[3])
plt.show()