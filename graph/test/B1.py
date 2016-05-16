def check(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != matrix[j][i]:
                return 'NO'
    return 'YES'

N = int(input())

matrix = []

for i in range(N):
    data = str(input()).split()
    matrix.append(data)

print(check(matrix))

