data = str(input()).split()
n, m = int(data[0]), int(data[1])
matrix = [[0]*n for i in range(n)]
for i in range(m):
    line = str(input()).split()
    for j in range(n):
        if j+1 == int(line[0]):
            for k in range(n):
                if k+1 == int(line[1]):
                    matrix[j][k] = 1
for line in matrix:
    for element in line:
        print(element, end=' ')
    print(end='\n')