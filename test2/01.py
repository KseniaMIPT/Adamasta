import pprint
n = int(input())
parents = {}
line = input().split()
parents[line[0]] = line[1]
parents[line[1]] = None
for i in range(n-2):
    line = input().split()
    parents[line[0]] = line[1]
pprint.pprint(parents)
