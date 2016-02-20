__author__ = 'student'
f = open('input.txt', 'r')
f = f.read()
f = f.lower()
for i in range(len(f)):
    if (f[i] == '!') or (f[i] == ',') or (f[i] == '.') or (f[i] == '?'):
        f = f[:f.index(f[i])] + ' ' + f[f.index(f[i])+1:]

F = []
Words = f.split()

D = dict()

for i in range(len(Words)):
    if Words[i] not in D:
        D[Words[i]] = 1
    else:
        D[Words[i]] += 1
max = 0
for i in D:
    if D[i] > max:
        max = D[i]
        max_word = i
print(max_word, max)



