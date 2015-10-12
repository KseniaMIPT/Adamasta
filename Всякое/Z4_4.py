A = [1, 2, 3, 2, 3, 3]
a = -1
max = 0
for i in range(len(A)):
    a += 1
    b = A.count(A[a])
    if b > max:
        max = b
print(max)