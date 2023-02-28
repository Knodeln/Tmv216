import numpy as np
from scipy import linalg as LA
from sympy import Matrix
from sympy import zeros
from sympy import shape
import time

def random_matrix(i):
    A = zeros(i, i)
    for x in range(i*i):
        A[x] = np.random.randint(-10, 10)
    b = zeros(i, 1)
    for x in range(i):
        b[x] = np.random.randint(-10, 10)
    T = A.row_join(b)
    time1 = time.time()
    Tref = T.rref()
    time2 = time.time()
    print(Tref)
    print(time2-time1)


def main():
    # uppgift a)

    time1 = time.time()
    A1 = Matrix([[1, 2, 1, -1, 2], [3, 4, 5, 2, 0], [2, 2, 1, 0, 2]])
    b1 = Matrix([[0], [0], [0]])
    T1 = A1.row_join(b1)
    time2 = time.time()
    time3 = time2 - time1
    print("It took " + str(time3) + " secconds")
    Aref = T1.rref()
    print(Aref)
    # Eftersom det inte finns en rad för att lösa x4 och x5 sätter man dem som s och t,
    # utifrån det får man ut lösningar för x1-x3 vilket kan skrivas på parameter form som;
    # x = s[-1,3/2,-1,1,0] + t[0,-5/3,4/3,0,1]

    # uppgift b)

    random_matrix(100)
    # Tiden för att utföra funktionen rref ökar exponensiellt och med en 100x100 matris
    # tar det alldelles för lång tid för att ge ett svar.

if __name__ == "__main__":
    main()