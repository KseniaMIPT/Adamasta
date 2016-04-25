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


graph = graph_from_input()

sort = sorted(graph)

for key in sort:
    print(key, len(graph[key]))

