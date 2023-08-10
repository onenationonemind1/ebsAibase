A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in range(0, 3):
    for j in range(0, 3):
        A[i][j] = ((i + 1) * (i + 1)) + ((j + 1) * (j + 1))

print(A)

for i in range(0, 3):
    for j in range(0, 3):
        B[i][j] = (i + 1) * (j + 1)

print(B)

for i in range(0, 3):
    for j in range(0, 3):
        C[i][j] = A[i][j] - (2 * B[i][j])

print(C)
