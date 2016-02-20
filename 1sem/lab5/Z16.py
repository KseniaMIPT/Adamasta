n = int(input())
A = [[1] * k for k in range(1, n + 2)]
for i in range(2, n + 1):
    for j in range(1, len(A[i]) - 1):
        A[i][j] = A[i-1][j-1] + A[i-1][j]
for i in range(len(A)):
    print(A[i])