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

node_list = []
set = set()
for key in g:
    if key not in set:
        node_list.append(key)
        set.add(key)
    if g[key]:
        if g[key] not in set:
            set.add(g[key])
            node_list.append(g[key])
sort_nodes = sorted(node_list)

for i in range(len(sort_nodes)):
    h = 0
    node = sort_nodes[i]
    while g[node]:
        h += 1
        node = g[node]
    print(sort_nodes[i], h)