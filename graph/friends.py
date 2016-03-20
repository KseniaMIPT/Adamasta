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


def bfs_fire(g, start, fired=set()):
    """Функция возвращаем множество вершин графа, входящих в компоненту связности.
    :param g: основной граф
    :param start: начальная вершина
    :return fired: множество вершин графа, входящих в компоненту связности
    """
    fired.add(start)
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in g[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                queue.append(neighbour)
    return fired


def draw_graph(g, tree):
    """Функция рисует граф и остовое дерево.
    :param g: основной граф
    :param tree: остовое дерево
    """
    pos = nx.spring_layout(g)
    # Рисуем вершины основного графа
    nx.draw_networkx_nodes(g, pos, node_size=1700, node_color='white', linewidths=0.5, alpha=0.9)
    # Рисуем вершины компоненты связности
    nx.draw_networkx_nodes(g, pos, node_size=1700, node_color='#82C5D3', linewidths=0.5, alpha=0.5, nodelist=tree)
    # Рисуем ребра графа
    nx.draw_networkx_edges(g, pos, width=2, alpha=1, edge_color='k')
    # Рисуем метки
    nx.draw_networkx_labels(g, pos, font_size=12, font_family='sans-serif')


def check_connection(graph):
    """
    :param graph: граф, который проверяется на связность
    :return: true/false в зависимости от того, связан граф или нет
    """
    for node in graph:
        if len(graph) == len(bfs_fire(graph, node)):
            pass
        else:
            return False
    return True


def draw_graph_components(graph):
    """Функция выводит на отдельных изображениях графы с их компонентами связности.
    :param graph: граф с искомыми компонентами связности
    """
    if check_connection(graph):
        draw_graph(graph, graph)
    else:
        called_components = []  # Список из пройденных компонент
        number = 0  # Нормер компоненты
        for node in graph:  # Перебираем вершины в графе
            current_fired = bfs_fire(graph, node, fired=set())
            count = 0
            for element in called_components:
                if current_fired != element:
                    count += 1
            if count == len(called_components):
                number += 1
                component = graph.copy().subgraph(current_fired)
                plt.figure(number)
                draw_graph(graph, component)
                called_components.append(current_fired.copy())
    plt.show()

# Считываем граф
graph = graph_input()

# Проверяем связность графа
if check_connection(graph):
    print('Граф является связным')
else:
    print('Граф не является связным')

# Рисуем графы и их компоненты связности
draw_graph_components(graph)
