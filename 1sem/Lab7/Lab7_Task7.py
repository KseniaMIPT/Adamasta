import numpy as np
import matplotlib.pyplot as plt
import math

a = 3
b = 0.5
x = np.arange(-2, 2, 0.01)
y = x.copy()
def func(x):
    for i in range(len(x)):
        y[i] = sum([(b ** n) * math.cos((a ** n) * math.pi * x[i]) for n in range(100)])
    return y
plt.plot(x, func(x))
plt.show()