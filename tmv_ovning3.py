import numpy as np



def main():
    bilcalc(1 / 3, 1 / 3, 1 / 3, 100000)
    print("")
    bilcalc2(1 / 3, 1 / 3, 1 / 3, 100000)
    print("")
    bilcalc2(0, 1, 0, 100000)
    # bilcalc(1 / 3, 1 / 3, 1 / 3, 10)
    # print("")
    # bilcalc(1 / 3, 1 / 3, 1 / 3, 100)
    # print("")
    # bilcalc(1 / 3, 1 / 3, 1 / 3, 1000)
    # print("")
    # bilcalc(1 / 3, 1 / 3, 1 / 3, 10000)
    # print("")
    # bilcalc(1 / 3, 1 / 3, 1 / 3, 100000)

    # print("")
    # bilcalc(1, 0, 0, 100000)
    # print("")
    # bilcalc(0, 1, 0, 100000)
    # print("")
    # bilcalc(0, 0, 1, 100000)

# Med "rå" matte
def bilcalc(c, l, u, veckor):
    i = 0
    while i < veckor:
        c_temp = c
        l_temp = l
        u_temp = u
        c = 0.7 * c_temp + 0.1 * l_temp + 0.3 * u_temp
        l = 0.1 * c_temp + 0.6 * l_temp + 0.2 * u_temp
        u = 0.2 * c_temp + 0.3 * l_temp + 0.5 * u_temp

        i += 1
    print(str(c) + " Central bilar efter " + str(veckor) + " veckor")
    print(str(l) + " Landvetter bilar efter " + str(veckor) + " veckor")
    print(str(u) + " Uthyrda bilar efter " + str(veckor) + " veckor")


# Med matris matte
def bilcalc2(c, l, u, veckor):
    i = 0
    v = np.array([[c], [l], [u]])
    A = np.array([[0.7, 0.1, 0.3],
                  [0.1, 0.6, 0.2],
                  [0.2, 0.3, 0.5]])
    while i < veckor:
        v = np.matmul(A, v)
        i +=1
    print(v)



if __name__ == "__main__":
    main()
