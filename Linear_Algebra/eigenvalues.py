# eigenvalues.py

import numpy as np

print("=== EIGENVALUES AND EIGENVECTORS ===\n")

A = np.array([[4, 2],
              [1, 3]])

print("Matrix A:")
print(A)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

print("\n=== PROGRAM COMPLETED ===")
