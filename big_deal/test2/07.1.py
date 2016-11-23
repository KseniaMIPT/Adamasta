N = int(input())
vertexes = set()
def graph_from_input():
    graph = {}
    for i in range(N-1):
        a, b = [x for x in input().split()]
        vertexes.add(a)
        vertexes.add(b)
        if a not in graph:
            graph[a] = b
    for v in vertexes:
        if v not in graph:
            graph[v] = None
    return graph
g = graph_from_input()
node = str(input())

while g[node]:
    print(g[node])
    node = g[node]