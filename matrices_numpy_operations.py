import numpy as np

X = np.array([[0, 1, 1], [1, 0, 1]])
Y = np.array([[1, 1], [1, 1], [-1, 1]])

Z = np.array([[1, 1], [2, 2], [3, 3]])

print(Z)

print(Z.T)

print(np.dot(X, Y))
