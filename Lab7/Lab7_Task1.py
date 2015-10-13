__author__ = 'student'
import math
def f(x):
    if ((5/4) + (1/x**15)) != 0:
        x = float(x)
        y = float()
        y = math.log((1/(math.exp(math.sin(x) + 1)))/((5/4) + (1/x**(15))), 1 + x**2)
        return y
    else:
        return 'Sorry'
print(f(1))
print(f(10))
print(f(1000))