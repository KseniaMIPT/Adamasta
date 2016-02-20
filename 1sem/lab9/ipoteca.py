from decimal import *
S = int(input())
x = float(input())
y = int(input())
def pay(S, x, y):
    p = x/1200
    x = S * p * ((1 + p)**(y * 12)) / (-1 + (1 + p) ** (y * 12))
    return x
def dpay(S, x, y):
    x = pay(S, x, y) * 12 * y - S
    return x
val1 = Decimal(pay(S, x, y)).quantize(Decimal('0.01'))
val2 = Decimal(dpay(S, x, y)).quantize(Decimal('0.01'))

print(val1, val2)
