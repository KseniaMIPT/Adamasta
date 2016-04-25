def digraph_from_input():
    N = int(input())
    digraph = {}
    for i in range(N):
        line = input().split()
        if line[0] not in digraph:
            digraph[line[0]] = {line[1]}
        else:
            digraph[line[0]].add(line[1])
        if line[1] not in digraph:
            digraph[line[1]] = set()
    return digraph


def deikstra(g, start):
    """Функция возвращает словарь из кратчайших путей от заданной вершины до всех остальных.
    :param g: данный граф
    :param start: начальная вершина
    """
    shortest_distance = {vertex: float('+inf') for vertex in g}
    shortest_distance[start] = 0
    shortest_way = {vertex: [] for vertex in g}
    shortest_way[start] = []
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in g[current]:
            if shortest_distance[current] + 1 < shortest_distance[neighbour]:
                shortest_distance[neighbour] = shortest_distance[current] + 1
                shortest_way[neighbour].append(current)
                shortest_way[neighbour] += shortest_way[current][:]
                queue.append(neighbour)
    return [shortest_way, shortest_distance]

digraph = digraph_from_input()
start_node = str(input())
ways = deikstra(digraph, start_node)[0]
m = int(input())
for i in range(m):
    node = str(input())
    if node == start_node:
        print(start_node)
    else:
        way = ways[node]
        if len(way) < 1:
            print(-1)
        else:
            for i in range(len(way)):
                print(way[(-1)*(i+1)], end = ' ')
            print(node)
