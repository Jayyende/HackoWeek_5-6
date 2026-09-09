# calculus_problems.py

print("=== CALCULUS PRACTICE PROBLEMS ===\n")

# Problem 1
print("Derivative of x²:")
x = 5
print("2x =", 2*x)

# Problem 2
print("\nDerivative of x³:")
print("3x² =", 3*(x**2))

# Problem 3
print("\nDerivative of 5x²:")
print("10x =", 10*x)

# Problem 4
print("\nDerivative of sin(x)")
print("Formula = cos(x)")

# Problem 5
print("\nDerivative of ln(x)")
print("Formula = 1/x")

# Problem 6
print("\nGradient of f(x,y)=x²+y²")

x = 3
y = 4

dx = 2*x
dy = 2*y

print("Gradient =", [dx, dy])

# Problem 7
print("\nGradient of x²+3y²")

dx = 2*x
dy = 6*y

print("Gradient =", [dx, dy])

# Problem 8
print("\nGradient Magnitude")

magnitude = (dx**2 + dy**2)**0.5

print(magnitude)

# Problem 9
print("\nChain Rule Example")
print("d/dx[(x²+1)³]")
print("= 6x(x²+1)²")

print("\n=== COMPLETED ===")
