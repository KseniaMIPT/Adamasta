A =[1,2,3,4,5,6,7]
n = -1
for i in range(len(A) // 2):
    n += 2
    A.insert(n, A[-1])
    A.pop()
print(A)