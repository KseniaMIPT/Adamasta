def graph_from_input():
    N = int(input())
    graph = {}
    for i in range(N):
        line = input().split()
        if line[0] not in graph:
            graph[line[0]] = {line[1]}
        else:
            graph[line[0]].add(line[1])
        if line[1] not in graph:
            graph[line[1]] = {line[0]}
        else:
            graph[line[1]].add(line[0])
    return graph


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
        return 1
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
                called_components.append(current_fired.copy())
        return number


graph = graph_from_input()
print(draw_graph_components(graph))
