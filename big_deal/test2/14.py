def digraph_from_input():
    N = int(input())
    digraph = {}
    for i in range(N-1):
        line = input().split()
        if line[1] not in digraph:
            digraph[line[1]] = {line[0]}
        else:
            digraph[line[1]].add(line[0])
        if line[0] not in digraph:
            digraph[line[0]] = set()
    return digraph

digraph = digraph_from_input()
start_node = str(input())

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

tree = bfs_fire(digraph, start_node)
