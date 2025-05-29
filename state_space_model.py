import numpy as np

class state_space_model:
    def __init__(self, init_state_vector=np.zeros(2), A=None, B=None, C=None, D=None):
        self.state_vector_length = init_state_vector.size
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.x = init_state_vector

        self.x_history = []
        self.y_history = []
        self.u_history = []

    def step(self, dt, u=None):
        if u == None:
            u = np.zeros(self.state_vector_length)
        self.x += (np.matmul(self.A, self.x) + np.matmul(self.B, u))*dt
        y = np.matmul(self.C, self.x) + np.matmul(self.D, u)
        self.x_history.append(self.x)
        self.y_history.append(y)
        self.u_history.append(u)

    def measure(self):
        return self.y_history[-1] + np.random.normal(loc=0.0, scale=0.0002, size=self.state_vector_length)

        
A = np.array([[0.0,1.0], [0.0,0.0]])
B = np.zeros([2,2])
C = np.array([[1.0,0.0], [0.0, 1.0]])
D = np.zeros([2,2])
init_sv = np.array([0.0, 1.0])
model = state_space_model(init_state_vector=init_sv, A=A, B=B, C=C, D=D)
for i in range(10):
    model.step(0.01)
    print(model.measure())