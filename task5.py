from random import *
data = open('int_data.txt','w')
S = []
for i in range(1000000):
    x = randint(0,100)
    S.append(x)
data.write(str(S))
data.close()