import pprint
N = int(input())
g = {}
for i in range(N-1):
    line = str(input()).split()
    try:
        g[line[1]].add(line[0])
    except KeyError:
        g[line[1]] = set()
        g[line[1]].add(line[0])
    try:
        if len(g[line[0]]) != 0:
            g[line[0]] = g[line[0]]
    except Exception:
        g[line[0]] = set()

node_list = []
set = set()
for key in g:
    if key not in set:
        node_list.append(key)
        set.add(key)
    for child in g[key]:
        if child not in set:
            set.add(child)
            node_list.append(child)
sort_nodes = sorted(node_list)
for node in sort_nodes:
    print(node, len(g[node]))
