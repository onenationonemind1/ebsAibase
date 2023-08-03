A_sum_B = [[1, 3], [0, 1]]
B_sum_C = [[2, 1], [-1, 1]]
C_sub_A = [[0, 0], [0, 0]]
for i in range (0, 2) :
    for j in range (0, 2) :
        C_sub_A[i][j] = B_sum_C[i][j] - A_sum_B[i][j]
        print(C_sub_A)
