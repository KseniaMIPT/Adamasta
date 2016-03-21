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


def floyd(graph):
    f = graph.copy()
    for node1 in graph:
        for node2 in graph:
            for node3 in graph:
                f[node2][node3] = min(f[node2][node3], f[node2][node1] + f[node1][node3])
    return f


graph = graph_input()
f = floyd(graph)
print(f)