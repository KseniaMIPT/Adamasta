import pprint


def graph_from_input():
    N = int(input())
    graph = {}
    for i in range(N):
        line = input().split()
        if line[0] not in graph:
            graph[line[0]] = {line[1]}
        else:
            graph[line[0]].add(line[1])
        if line[1] not in graph:
            graph[line[1]] = {line[0]}
        else:
            graph[line[1]].add(line[0])
    return graph


def m_graph(graph):
    new_graph = {}
    node_set = set()
    for key in graph:
        if key not in node_set:
            node_set.add(key)
        for node in graph[key]:
            if node not in node_set:
                node_set.add(node)
    for node in node_set:
        new_graph[node] = set()
    for key in graph:
        for element in node_set:
            if element not in graph[key] and element != key:
                new_graph[key].add(element)
    return new_graph

graph = graph_from_input()
m_graph = m_graph(graph)

pprint.pprint(m_graph)