n = int(input())
Time = [[0, 0] for i in range(n)]
for i in range(n):
    t = list(map(int, str(input()).split()))
    Time[i][0] = t[0]
    Time[i][1] = t[1]
t = int(input())
count = 0
for i in range(n):
    if Time[i][0] == t: count += 1
    if Time[i][1] == t: count += 1
    if Time[i][0] < t and Time[i][1] > t: count += 1
print(count)