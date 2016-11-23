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
pprint.pprint(g)
