n = int(input())
edges = []
for i in range(n):
    line = str(input()).split()
    for j in range(n):
        if int(line[j]) == 1:
            edges.append([i+1, j+1])
for edge in edges:
    print(edge[0],edge[1])