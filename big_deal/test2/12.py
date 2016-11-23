N = int(input())

children = {}

for i in range(N - 1):
    a, b = input().split()
    if b not in children:
        children[b] = {a}
    else:
        children[b].add(a)

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
    old, young = b, a
    S = [old]
    while S:
        curr = S.pop()
        if curr == young: return True
        for i in children[curr]:
            S.append(i)
    return False


M = int(input())
for i in range(M):
    a, b = input().split()
    if a == b or check(b, a):
        print(1)
    elif check(a, b):
        print(2)
    else:
        print(0)
