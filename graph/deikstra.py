import networkx as nx
import matplotlib.pyplot as plt


def graph_input():
    """Функция считывает граф из файла."""
    file = open('graph.txt', 'r')  # Открываем файл со списком ребер
    g = nx.Graph()                 # Создаем заготовку под граф
    for line in file.readlines():  # Производим считывание ребер из файла
        a, b, weight = line.split()
        a, b, weight = str(a), str(b), int(weight)
        g.add_edge(a, b, weight=weight)
    file.close()  # закрываем файл
    return g


def deikstra(g, start):
    """Функция возвращает словарь из кратчайших путей от заданной вершины до всех остальных.
    :param g: данный граф
    :param start: начальная вершина
    """
    shortest_path = {vertex: float('+inf') for vertex in g}
    shortest_path[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in g[current]:
            if shortest_path[current] + g[current][neighbour]['weight'] < shortest_path[neighbour]:
                shortest_path[neighbour] = shortest_path[current] + g[current][neighbour]['weight']
                queue.append(neighbour)
    return shortest_path

graph = graph_input()
for node in graph:
    shortest_path = deikstra(graph, node)
    print('Длины кратчайших путей от', node, 'до', shortest_path)
