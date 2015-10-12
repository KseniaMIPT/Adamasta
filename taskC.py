A = input().split()
T1 = A[0]
T2 = A[1]
T1 = T1.split(':')
T2 = T2.split('.')
if T2[0] == 'a':
    if T1[0] == '12':
        x = '00'
    elif int(T1[0]) <= 9:
        x = str()
        x = '0' + T1[0]
    else:
        x = T1[0]
else:
    x = int(T1[0]) + 12
y = T1[-1]
print(x,':',y, sep='')