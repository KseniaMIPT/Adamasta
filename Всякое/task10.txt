A = [1,2,3,4,2]
t = 2
for i in range(t):
    A.insert((- int(A[-1])) - 1, A[-1])
    A.pop()
print(A)