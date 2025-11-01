import numpy as np
import quaternion

class solid_body:
    def __init__(self, q_init, omega_init, pos_init, vel_init):
        # "I" is the inertial reference frame
        # attitude
        self.orientation_quaternion_I = q_init
        self.angular_velocity_vector_I = omega_init

        # translation
        self.position_vector_I = pos_init
        self.velocity_vector_I = vel_init
    
    def apply_torque(self, torque_vector):
        pass

    def apply_force(self, force_vector):
        pass

    def integration_step(self, delta_time):
        self.orientation_quaternion_I += self.dq_dt()*delta_time
        if self.orientation_quaternion_I[3] < 0:
            self.orientation_quaternion_I = -self.orientation_quaternion_I
        self.orientation_quaternion_I /= np.linalg.norm(self.orientation_quaternion_I, ord=2)
        
    def dq_dt(self):
        angular_vel =  np.array([self.angular_velocity_vector_I[0], self.angular_velocity_vector_I[1], self.angular_velocity_vector_I[2], 0.0])
        return 0.5*quaternion.quat_mul(self.orientation_quaternion_I, angular_vel)
    

    


    