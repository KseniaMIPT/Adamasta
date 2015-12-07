from decimal import *
x0 = Decimal('4')
x1 = Decimal('4.25')
def f(y,z):
    return 108 - (815 - 1500/z) / y
for i in range(31):
    x0, x1 = x1, x0
    x1 = f(x1, x0)
print(x1)
