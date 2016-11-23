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

data = digraph_from_input()
g =
start_node = data[1]
#start_node =
print(g)

h = {node:0 for node in node_list}

def bfs_fire(g, start, h, fired=set(), tree =[], n=-1):
    """Функция выделяет остовое дерево методом обхода в ширину.
    :param g: основной граф
    :param start: начальная вершина
    :param fired: множество уже имеющихся в графе вершин
    :return tree: остовое дерево
    """
    fired.add(start)
    queue = [start]
    n += 1
    while queue:
        current = queue.pop(0)
        h[current] = n
        for neighbour in g[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                queue.append(neighbour)
                tree.append([current, neighbour])
    return h

dict = bfs_fire(g, start_node, h)
print(dict)
#print(tree)
#print(tree[0][0])
#for element in tree:
#    print(element[1])