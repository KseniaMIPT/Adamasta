n = int(input())

children = {}

for i in range(n - 1):
    son, father = input().split()
    if father not in children:
        children[father] = {son}
    else:
        children[father].add(son)

called = set()

parents = {}

for i in children:
    called.add(i)
    for j in children[i]:
        parents[j] = i
        called.add(j)

for i in called:
    if i not in children:
        children[i] = set()
    if i not in parents:
        parents[i] = None

for i in parents:
    if parents[i] == None and children[i] != None:
        root = i

def check(a, b):
    start_node = {root}
    current_node = a
    while current_node != root:
        start_node.add(current_node)
        current_node = parents[current_node]
    current_node = b
    while current_node not in start_node:
        curr = parents[current_node]
    return current_node

M = int(input())
for i in range(M):
    a, b = input().split()
    print(check(a, b))
