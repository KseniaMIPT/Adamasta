n = int(input())
data = list(map(int, str(input()).split()))
k = int(input())
max = 0
for i in range(n - 2):
    t = data[i] + data[i+1] + data[i+2]
    if t > max:
        max = t
print(max)