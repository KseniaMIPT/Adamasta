__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10.01,0.01)
plt.plot(x,x*x - 6 - x)
plt.show()