import pprint
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
    tree = []
    while queue:
        current = queue.pop(0)
        for neighbour in g[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                queue.append(neighbour)
                tree.append([current, neighbour])
    return tree

digraph = digraph_from_input()
start_node = str(input())
tree_graph = bfs_fire(digraph, start_node)
parents = {}
parents[start_node] = None
for i in range(len(tree_graph)):
    parents[tree_graph[i][1]] = tree_graph[i][0]
pprint.pprint(parents)
