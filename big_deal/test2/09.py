def digraph_from_input():
    N = int(input())
    digraph = {}
    for i in range(N-1):
        line = input().split()
        if line[1] not in digraph:
            digraph[line[1]] = {line[0]}
        else:
            digraph[line[1]].add(line[0])
        if line[0] not in digraph:
            digraph[line[0]] = set()
    return digraph

digraph = digraph_from_input()
start_node = str(input())

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

tree = call_friends(digraph, start_node)
#print(tree)
print(tree[0][0])
for element in tree:
    print(element[1])

