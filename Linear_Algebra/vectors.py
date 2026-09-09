# vectors.py

import numpy as np

print("=== VECTOR OPERATIONS ===\n")

# Creating vectors
v1 = np.array([2, 3])
v2 = np.array([4, 5])

print("Vector 1:", v1)
print("Vector 2:", v2)

# Magnitude
print("\nMagnitude of Vector 1:")
print(np.linalg.norm(v1))

# Addition
print("\nVector Addition:")
print(v1 + v2)

# Subtraction
print("\nVector Subtraction:")
print(v1 - v2)

# Scalar Multiplication
print("\nScalar Multiplication (2 × v1):")
print(2 * v1)

# Dot Product
print("\nDot Product:")
print(np.dot(v1, v2))

# Unit Vector
print("\nUnit Vector of v1:")
unit_vector = v1 / np.linalg.norm(v1)
print(unit_vector)

print("\n=== PROGRAM COMPLETED SUCCESSFULLY ===")
