import numpy as np  # 벡터, 행렬 데이터를 쉽게 처리하기 위한 모듈

A = [[0, 0, 0, 0], [0, 0, 0, 0]]
sum = 0

for i in range(0, 2):
    for j in range(0, 4):
        A[i][j] = i + 1 + j + 1
        print(A[i][j])
        sum = sum + A[i][j]

print("sum = ", sum)
