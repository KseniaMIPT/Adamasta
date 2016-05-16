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
    return called

def check(graph):
    called = call_friends(graph, 0)
    for node in graph:
        if node not in called:
            return 'NO'
    return 'YES'

def graph_components(graph, nodes):
    """Функция выводит на отдельных изображениях графы с их компонентами связности.
    :param graph: граф с искомыми компонентами связности
    """
    if check(graph) == 'YES':
        return 1
    else:
        called_nodes = set()
        number = 0
        while len(called_nodes) != nodes:
            for node in graph:
                if node not in called_nodes:
                    called_nodes.add(node)
                    number += 1
                    called_nodes.update(call_friends(graph, node))
        return number


N = int(input())  # количество вершин
M = int(input())  # количество ребер
graph = {}
for i in range(N):
    graph[i] = []

for i in range(M):
    data = str(input()).split()
    graph[int(data[0])].append(int(data[1]))
    graph[int(data[1])].append(int(data[0]))

print(graph_components(graph, N))
