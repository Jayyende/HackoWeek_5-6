# vector_problems.py

import numpy as np

print("=== VECTOR PRACTICE PROBLEMS ===\n")

# Problem 1
v = np.array([3, 4])
print("Problem 1: Magnitude of [3,4]")
print("Answer:", np.linalg.norm(v))

# Problem 2
A = np.array([2, 3])
B = np.array([4, 5])

print("\nProblem 2: Vector Addition")
print(A + B)

# Problem 3
A = np.array([8, 6])
B = np.array([3, 2])

print("\nProblem 3: Vector Subtraction")
print(A - B)

# Problem 4
v = np.array([2, 4])

print("\nProblem 4: Scalar Multiplication")
print(3 * v)

# Problem 5
A = np.array([1, 2])
B = np.array([3, 4])

print("\nProblem 5: Dot Product")
print(np.dot(A, B))

# Problem 6
v = np.array([3, 4])

print("\nProblem 6: Unit Vector")
print(v / np.linalg.norm(v))

print("\n=== COMPLETED ===")
