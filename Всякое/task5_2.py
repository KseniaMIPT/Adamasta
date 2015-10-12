from random import *
f = open('float_data.txt', 'w')
S = []
for i in range(1000000):
    x = "%.2f" %float(randint(0,100) + random())
    S.append(x)
f.write(str(S))
f.close()