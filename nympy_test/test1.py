import numpy as np
X = np.random.normal(loc=1, scale=10, size=(1000, 50))
m = np.mean(X, axis=0)
std = np.std(X)
print(X)
