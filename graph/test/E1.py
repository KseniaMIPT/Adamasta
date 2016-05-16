def call_friends(g, start, fired=set()):
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


def check(graph, nodes):
    for node in graph:
        called = call_friends(graph, node, fired=set())
        if len(called) != nodes:
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

print(check(graph, N))