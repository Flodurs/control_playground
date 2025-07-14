import numpy as np

class sat_equations_of_motion:
    def __init__(self):
        self.inertial_frame = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        