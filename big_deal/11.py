import pprint
graph = eval(input())
for key in graph:
    for node in graph[key]:
        if node not in graph:
            graph[node] = set()
        if key not in graph[node]:
            graph[node].add(key)
pprint.pprint(graph)