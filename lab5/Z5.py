from random import *
data = open('int_data.txt','w')
S = str()
for i in range(100):
    x = str(randint(0,100))
    S += x + ' '
data.write(str(S))
data.close()

from random import *
f = open('float_data.txt', 'w')
S = str()
for i in range(100):
    x = "%.2f" %float(randint(0,100) + random())
    S += x + ' '
f.write(str(S))
f.close()
