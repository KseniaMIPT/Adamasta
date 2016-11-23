import pprint
N = int(input())
list = []
for i in range(N-1):
    list.append(str(input()))

vertexes = set()
def graph_from_input():
    graph = {}
    for element in list:
        a, b = element.split()
        vertexes.add(a)
        vertexes.add(b)
        if a not in graph:
            graph[a] = b
    for v in vertexes:
        if v not in graph:
            graph[v] = None
    return graph
parents = graph_from_input()
#pprint.pprint(g)

g = {}
for element in list:
    line = element.split()
    try:
        g[line[1]].add(line[0])
    except KeyError:
        g[line[1]] = set()
        g[line[1]].add(line[0])
    try:
        if len(g[line[0]]) != 0:
            g[line[0]] = g[line[0]]
    except Exception:
        g[line[0]] = set()
root = None
for key in parents:
    if parents[key] == None:
        root = key
print =(root, parents, g)
pprint.pprint(print)