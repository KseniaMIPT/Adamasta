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


def draw_graph(g, tree):
    """Функция рисует граф с деревом.
    :param g: основной граф,
    :param tree: остовое дерево основного графа
    """
    pos = nx.spring_layout(g)

    nx.draw_networkx_nodes(g, pos, node_size=1700, node_color='white', linewidths=0.5, alpha=0.9)  # Рисуем вершины
    nx.draw_networkx_edges(g, pos, width=2, alpha=1, edge_color='k')  # Рисуем ребра основного графа
    nx.draw_networkx_edges(g, pos, edgelist=tree, width=8, alpha=0.8, edge_color='#82C5D3')  # Рисуем ребра дерева
    nx.draw_networkx_labels(g, pos, font_size=12, font_family='sans-serif')  # Рисуем метки

    plt.axis('off')
    plt.savefig("fruitland_dfs.png")
    plt.show()


graph = graph_input()
tree_graph = call_friends(graph, 'apple')
draw_graph(graph, tree_graph)
