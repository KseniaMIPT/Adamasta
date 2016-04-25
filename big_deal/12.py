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


def not_digraph(digraph):
    graph = copy.deepcopy(digraph)
    for key in graph:
        graph[key] = list(graph[key])
    for key in graph:
        for node in graph[key]:
            if node not in graph:
                graph[node] = []
            graph[node].append(key)
    return graph


def indegree(graph, start):
    sum = 0
    for key in graph:
        for node in graph[key]:
            if node == start:
                sum += 1
    return sum

digraph = digraph_from_input()
graph = not_digraph(digraph)

sort = sorted(copy.deepcopy(graph))

for key in sort:
    print(key, indegree(digraph, key), len(digraph[key]))
