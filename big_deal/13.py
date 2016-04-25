import pprint
import copy


def digraph_from_input():
    N = int(input())
    digraph = {}
    for i in range(N):
        line = input().split()
        if line[0] not in digraph:
            digraph[line[0]] = {line[1]}
        else:
            digraph[line[0]].add(line[1])
        if line[1] not in digraph:
            digraph[line[1]] = set()
    return digraph

def square_graph(graph):
    new_graph = copy.deepcopy(graph)
    for key in graph:
        for node in graph[key]:
            for far_node in graph[node]:
                if far_node not in graph[key]:
                    new_graph[key].add(far_node)
    return new_graph

digraph = digraph_from_input()
graph = square_graph(digraph)
pprint.pprint(graph)