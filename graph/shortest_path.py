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
    shortest_distance = {vertex: float('+inf') for vertex in g}
    shortest_distance[start] = 0
    shortest_way = {vertex: [] for vertex in g}
    shortest_way[start] = [start]
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in g[current]:
            if shortest_distance[current] + g[current][neighbour]['weight'] < shortest_distance[neighbour]:
                shortest_distance[neighbour] = shortest_distance[current] + g[current][neighbour]['weight']
                shortest_way[neighbour].append(current)
                queue.append(neighbour)
    return [shortest_way, shortest_distance]


def draw_graph(g1, g2):
    """Функция рисует граф и путь.
    :param g1: основной граф
    :param g2: путь
    """
    pos = nx.spring_layout(g1)
    # Рисуем вершины основного графа
    nx.draw_networkx_nodes(g1, pos, node_size=1700, node_color='white', linewidths=0.5, alpha=0.9)
    # Рисуем вершины пути
    nx.draw_networkx_nodes(g1, pos, node_size=1700, node_color='#82C5D3', linewidths=0.5, alpha=0.9, nodelist=g2)
    # Рисуем ребра графа
    nx.draw_networkx_edges(g1, pos, width=2, alpha=1, edge_color='k')
    # Рисуем метки
    nx.draw_networkx_labels(g1, pos, font_size=12, font_family='sans-serif')

    plt.axis('off')
    plt.savefig("fruitland_bfs.png")
    plt.show()


graph = graph_input()
start_node = str(input('Введите начальную вершину: '))
finish_node = str(input('Введите конечную вершину: '))

#start_node = 'apple'
#finish_node = 'plum'

shortest_way = deikstra(graph, start_node)[0][finish_node]        # Путь
shortest_distance = deikstra(graph, start_node)[-1][finish_node]  # Длина кратчайшего пути

if len(shortest_way) < 1:
    print('Путь отсутствует')
else:
    print('Путь из', start_node, 'в', finish_node, ':', shortest_way)
    print('Длина пути:', shortest_distance)

subgraph = set()
subgraph.add(start_node)
subgraph.add(finish_node)
for node in shortest_way:
    if node not in subgraph:
        subgraph.add(node)

draw_graph(graph, graph.subgraph(subgraph))
