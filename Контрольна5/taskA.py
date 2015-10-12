A = input().split()
x = 0
y = 0
while A[0] != 'Treasure!':
    if A[0] == 'West':
        x = x - int(A[1])
    if A[0] == 'South':
        y = y - int(A[1])
    if A[0] == 'East':
        x = x + int(A[1])
    if A[0] == 'North':
        y = y + int(A[1])
    A = input().split()
print(x, y)