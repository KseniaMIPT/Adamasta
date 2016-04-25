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


def call_friends(g, start, tree_graph=[], called=set()):
    """Функция выделяет остовое дерево в заданном графе методом обхода в глубину.
    :param start: начальная вершина
    :param called: вершины, которое уже содержит дерево
    :return tree_graph остовое дерево
    """
    called.add(start)
    for neighbour in g[start]:
        if not [start, neighbour] in tree_graph and neighbour not in called:
            tree_graph.append([start, neighbour])
            call_friends(g, neighbour, tree_graph, called)
    return tree_graph


digraph = digraph_from_input()
start_node = str(input())
tree_graph = call_friends(digraph, start_node)
print(tree_graph)
path = []
for i in range(len(tree_graph)):
    for j in range(2):
        if tree_graph[i][j] not in path:
            path.append(tree_graph[i][j])
for i in range(len(path)):
    print(path[i])