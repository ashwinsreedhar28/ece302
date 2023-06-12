import numpy as np
import matplotlib.pyplot as plt

# Part A
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 2, 3]).reshape(-1, 1)

mult = np.matmul(matrix, vector)
print(mult)

# Part B
x = np.linspace(-np.pi, np.pi, 1000)

y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Problem 9 (b): Sin Wave on [-pi, pi] with 1000 Points')

plt.show()

# Part C
rand_num = np.random.uniform(0, 1, 10000)

plt.hist(rand_num, bins=50, edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Problem 9 (c): Histogram of 10000 uniformly distributed random numbers on [0, 1)')

plt.show()