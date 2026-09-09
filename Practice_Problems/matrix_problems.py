# matrix_problems.py

import numpy as np

print("=== MATRIX PRACTICE PROBLEMS ===\n")

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Problem 1: Matrix Addition")
print(A + B)

print("\nProblem 2: Matrix Subtraction")
print(A - B)

print("\nProblem 3: Matrix Multiplication")
print(np.dot(A, B))

print("\nProblem 4: Matrix Transpose")
print(A.T)

print("\nProblem 5: Identity Matrix")
print(np.identity(3))

print("\n=== COMPLETED ===")
