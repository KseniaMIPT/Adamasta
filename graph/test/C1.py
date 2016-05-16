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

N = int(input())  # количество вершин
M = int(input())  # количество ребер
graph = {}
for i in range(N):
    graph[i] = []

for i in range(M):
    data = str(input()).split()
    graph[int(data[0])].append(int(data[1]))
    graph[int(data[1])].append(int(data[0]))

print(check(graph))


