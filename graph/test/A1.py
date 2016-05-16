N = int(input())  # количество вершин
M = int(input())  # количество вершин

matrix = [[0]*N for i in range(N)]

for i in range(M):
    data = str(input()).split()
    matrix[int(data[0])][int(data[1])] = matrix[int(data[1])][int(data[0])] = 1

for line in matrix:
    for element in line:
        print(element, end=' ')
    print(end='\n')