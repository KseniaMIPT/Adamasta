k = int(input())
n = int(input())
A = [1] * k
for i in range(n - k + 1):
    A.append(sum(A[-k:]))
print(A[-1])
