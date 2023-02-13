import matplotlib.pyplot as plt
import numpy as np

A1 = np.array([[0, 0], [0, 0.16]])
A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])
allaA = [A1,A2,A3,A4]

b1 = np.array([0, 0])
b2 = np.array([0 ,1.6])
b3 = np.array([0, 4.6])
b4 = np.array([0, 0.44])

allaB = [b1,b2,b3,b4]

v0 = np.array([0, 0])


def main(v0):
    n = 0

    while n < 4000:
        index = np.random.choice([0, 1, 2, 3], p=[0.01, 0.85, 0.07, 0.07])
        A = allaA[index]
        b = allaB[index]
        v0 = np.matmul(A, v0)
        v0 = np.add(v0, b)
        plt.plot(v0[0], v0[1], "bo")


        n += 1
    plt.show()


if __name__ == "__main__":
    main(v0)

