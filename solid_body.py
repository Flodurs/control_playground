import numpy as np
import quaternion

class solid_body:
    def __init__(self):
        # "I" is the inertial reference frame
        # attitude
        self.orientation_quaternion_I = None
        self.angular_velocity_vector_I = None

        # translation
        self.position_vector_I = None
        self.velocity_vector_I = None
    
    def apply_torque(self, torque_vector):
        pass

    def apply_force(self, force_vector):
        pass

    def integrate(self, delta_time):
        pass

    def dq_dt(self):
        return 0.5*quaternion.quat_passive_rotation(self.orientation_quaternion_I*np.array(self.angular_velocity_vector_I[0], 
                                                    self.angular_velocity_vector_I[1], 
                                                    self.angular_velocity_vector_I[2], 
                                                    0.0))
    


    