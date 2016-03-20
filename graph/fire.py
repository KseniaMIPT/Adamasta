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


def bfs_fire(g, start, fired=set(), tree =[]):
    """Функция выделяет остовое дерево методом обхода в ширину.
    :param g: основной граф
    :param start: начальная вершина
    :param fired: множество уже имеющихся в графе вершин
    :return tree: остовое дерево
    """
    fired.add(start)
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in g[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                queue.append(neighbour)
                tree.append([current, neighbour])
    return tree


def draw_graph(g, tree):
    """Функция рисует граф и остовое дерево.
    :param g: основной граф
    :param tree: остовое дерево
    """
    pos = nx.spring_layout(g)

    nx.draw_networkx_nodes(g, pos, node_size=1700, node_color='white', linewidths=0.5, alpha=0.9)  # Рисуем вершины
    nx.draw_networkx_edges(g, pos, width=2, alpha=1, edge_color='k')  # Рисуем ребра основного графа
    nx.draw_networkx_edges(g, pos, edgelist=tree, width=8, alpha=0.8, edge_color='#82C5D3')  # Рисуем ребра дерева
    nx.draw_networkx_labels(g, pos, font_size=12, font_family='sans-serif')  # Рисуем метки

    plt.axis('off')
    plt.savefig("fruitland_bfs.png")
    plt.show()


graph = graph_input()
tree = bfs_fire(graph, 'apple')
draw_graph(graph, tree)
