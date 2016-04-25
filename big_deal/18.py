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


def bfs_fire(g, start, fired=set()):
    """Функция выделяет остовое дерево методом обхода в ширину.
    :param g: основной граф
    :param start: начальная вершина
    :param fired: множество уже имеющихся в графе вершин
    :return tree: остовое дерево
    """
    fired.add(start)
    queue = [start]
    #tree = []
    while queue:
        current = queue.pop(0)
        for neighbour in g[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                queue.append(neighbour)
                #tree.append([current, neighbour])
    return fired


def check_path(graph, start_node, end):
    if end in bfs_fire(graph, start_node, set()):
        return 'YES'
    return 'NO'


graph = digraph_from_input()
n = int(input())
for i in range(n):
    line = input().split()
    start = line[0]
    end = line[1]
    print(check_path(graph, start, end))
