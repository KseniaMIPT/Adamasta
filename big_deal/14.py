import pprint


def t_graph(graph):
    new_graph = {}
    for key in graph:
        if key not in new_graph:
            new_graph[key] = set()
        for node in graph[key]:
            if node not in new_graph:
                new_graph[node] = set()
            new_graph[node].add(key)
    return new_graph

graph = eval(input())
t_graph = t_graph(graph)
pprint.pprint(t_graph)
