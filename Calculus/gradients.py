# gradients.py

print("=" * 50)
print("GRADIENTS IN MACHINE LEARNING")
print("=" * 50)

# Example Function:
# f(x,y) = x² + y²

def partial_x(x):
    return 2 * x

def partial_y(y):
    return 2 * y

# Sample Point
x = 3
y = 4

print("\nFunction:")
print("f(x,y) = x² + y²")

print("\nPoint:")
print(f"x = {x}")
print(f"y = {y}")

# Partial Derivatives
dx = partial_x(x)
dy = partial_y(y)

print("\nPartial Derivative wrt x:")
print(dx)

print("\nPartial Derivative wrt y:")
print(dy)

# Gradient Vector
gradient = [dx, dy]

print("\nGradient Vector:")
print(gradient)

# Magnitude of Gradient
magnitude = (dx**2 + dy**2) ** 0.5

print("\nMagnitude of Gradient:")
print(magnitude)

print("\nInterpretation:")
print("Gradient points toward maximum increase.")

print("\n" + "=" * 50)
print("PROGRAM EXECUTED SUCCESSFULLY")
print("=" * 50)
