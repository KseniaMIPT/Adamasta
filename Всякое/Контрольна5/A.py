input = open('input1.txt', 'r')
output = open('output1.txt', 'w')
T =[]
T = input.read()
A = list(map(int, T.split()))
n = 0

for i in range(A[0]):
    n += 1
    if A.count(A[n]) == 2:
        P = n
print(P)