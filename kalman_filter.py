import numpy as np
import state_space_model
import matplotlib.pyplot as plt


class kalman_filter:
    def __init__(self, init_state_vector=np.zeros(2), A=None, B=None, C=None, D=None):
        self.state_vector_length = init_state_vector.size
        self.x = init_state_vector
        self.P = np.identity(self.state_vector_length)


        # state space model
        self.A=A
        self.B=B
        self.C=C
        self.D=D

        # cov
        self.Q = np.diag([0.2, 0.2])
        self.R = np.diag((0.0, 0.10))

        # oberserver transform
        self.H = np.array([[0, 0],[0, 1]])


    def step(self, u, z):
        # prediction
        self.x = np.matmul(self.A, self.x) + np.matmul(self.B, u)
        self.P = np.matmul(np.matmul(self.A, self.P), np.transpose(self.A)) + self.Q

        print(f"Predicted x: {self.x}")
        print(f"Predicted P: {self.P}")
        print(f"m: {z}")
        #print(np.matmul(self.H, np.matmul(self.P, np.transpose(self.H))) + self.R)
        # correction
        K = np.matmul(np.matmul(self.P, np.transpose(self.H)), np.linalg.pinv(np.matmul(self.H, np.matmul(self.P, np.transpose(self.H))) + self.R))
        self.x = self.x + np.matmul(K, z - np.matmul(self.H, self.x))
        self.P = np.matmul(np.identity(self.state_vector_length)-np.matmul(K, self.H), self.P)

if __name__ == "__main__":
    A = np.array([[1.0,1.0], [0.0,1.0]])
    B = np.zeros([2,2])
    C = np.array([[1.0,0.0], [0.0, 1.0]])
    D = np.zeros([2,2])
    init_sv = np.array([0.0, 1.0])
    world = state_space_model.state_space_model(init_state_vector=init_sv, A=A, B=B, C=C, D=D)
    filter = kalman_filter(init_state_vector=init_sv, A=A, B=B, C=C, D=D)

    x_true = []
    x_estimate = []
    measurements = []
    errors = []


    fig, axs = plt.subplots(3)
    plt.ion()
    plt.show()
    fig.tight_layout()
    while True:
        
        measurement = world.measure()
        world.step()
        filter.step(np.zeros(2), measurement)
        

        x_true.append(world.x[0])
        x_estimate.append(filter.x[0])
        measurements.append(measurement[1])
        errors.append(abs(world.x[0]-filter.x[0]))
        print(f"True state: {world.x}")
        print(f"Estimated state: {filter.x}")
        print("-------------------------\n")
        
        for ax in axs:
            ax.clear()
        axs[0].plot(x_true, label="True x position [m]")
        axs[0].plot(x_estimate, label="Estimated x position [m]")
        axs[1].plot(measurements, label="Velocity measurements [m/s]")
        axs[2].plot(errors, label="Estimation error")
        for ax in axs:
            ax.legend()
        fig.canvas.draw()
        plt.pause(0.1)
