from fractions import *
x0 = Fraction(4,1)
x1 = Fraction(17,4)
def f(y,z):
    return  108 - (815 - 1500/z) / y
for i in range(31):
    x1, x0 = f(x1, x0), x1.limit_denominator(100000000000)
print(int(float(x1) + 0.5))
