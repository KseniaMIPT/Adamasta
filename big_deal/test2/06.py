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
list = []
for key in g:
    if len(g[key]) == 0:
        list.append(key)
sort_list = sorted(list)
for node in sort_list:
    print(node)