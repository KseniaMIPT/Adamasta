import matplotlib.pyplot as plt

input = open('float_data.txt', 'r')
numbers = list(map(float, input.read().split()))

plt.hist(numbers, bins=20)
plt.show()