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


def call_friends(g, start, tree_graph=[], called=set()):
    """Функция выделяет остовое дерево в заданном графе методом обхода в глубину.
    :param start: начальная вершина
    :param called: вершины, которое уже содержит дерево
    :return tree_graph остовое дерево
    """
    called.add(start)
    for neighbour in g[start]:
        if neighbour == main_node:
            return True, tree_graph
        if not [start, neighbour] in tree_graph and neighbour not in called:
            tree_graph.append([start, neighbour])
            call_friends(g, neighbour, tree_graph, called)



def node_list(graph):
    node_set = set()
    for key in graph:
        if key not in node_set:
            node_set.add(key)
        for node in graph[key]:
            if node not in node_set:
                node_set.add(node)
    return node_set


graph = graph_from_input()
nodes = node_list(graph)
flag = 0
for node in nodes:
    main_node = node
    current_result = call_friends(graph, node, tree_graph=[], called=set())
    print(node)
    print(current_result)
    if current_result:
        print(current_result)
        flag = 1
        break
if flag == 0:
    print('NO')
        #print(check(graph, nodes))
