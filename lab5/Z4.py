A = [1,2,3,4,5,6,7]
for i in range(0, len(A) - len(A) % 2, 2):
    A[i], A[i +1] = A[i + 1], A[i]
print(A)

A = [1, 2, 3, 4, 5]
A.insert(0,A[-1])
print(A[:-1])

A = [1,2,2,2,3,3,34,8]
B = str()
for i in range(len(A)):
    if A.count(A[i]) == 1:
        print(A[i])

A = [1, 2, 3, 2, 3, 3]
a = -1
max = 0
for i in range(len(A)):
    a += 1
    b = A.count(A[a])
    if b > max:
        max = b
print(max)
