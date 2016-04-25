#все плохо
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
            if neighbour == start_node:
                return ['Yes', ]
            if neighbour not in fired:
                fired.add(neighbour)
                queue.append(neighbour)
                tree.append([current, neighbour])
    #return tree


def call_friends(g, start, tree_graph=[], called=set()):
    """Функция выделяет остовое дерево в заданном графе методом обхода в глубину.
    :param start: начальная вершина
    :param called: вершины, которое уже содержит дерево
    :return tree_graph остовое дерево
    """
    called.add(start)
    for neighbour in g[start]:
        if neighbour == start_node:
            return ['YES', tree_graph]
        if not [start, neighbour] in tree_graph and neighbour not in called:
            tree_graph.append([start, neighbour])
            call_friends(g, neighbour, tree_graph, called)
    return ['NO']



digrahp = digraph_from_input()
start_node = str(input())
tree = call_friends(digrahp, start_node)
parents = {}
parents[start_node] = None
for i in range(len(tree)):
    parents[tree[i][1]] = tree[i][0]
pprint.pprint(parents)