# derivatives.py
# Demonstration of Derivatives using SymPy

from sympy import *

print("=" * 50)
print("DERIVATIVES IN CALCULUS")
print("=" * 50)

# Define variable
x = symbols('x')

# --------------------------------------------------
# Example 1: Polynomial Function
# --------------------------------------------------

print("\n1. POLYNOMIAL FUNCTION")

f1 = x**3 + 2*x**2 + x

print("Function:")
print("f(x) =", f1)

print("\nFirst Derivative:")
print(diff(f1, x))

# --------------------------------------------------
# Example 2: Second Derivative
# --------------------------------------------------

print("\n2. SECOND DERIVATIVE")

first_derivative = diff(f1, x)

second_derivative = diff(first_derivative, x)

print("First Derivative:")
print(first_derivative)

print("\nSecond Derivative:")
print(second_derivative)

# --------------------------------------------------
# Example 3: Exponential Function
# --------------------------------------------------

print("\n3. EXPONENTIAL FUNCTION")

f2 = exp(x)

print("Function:")
print("e^x")

print("\nDerivative:")
print(diff(f2, x))

# --------------------------------------------------
# Example 4: Logarithmic Function
# --------------------------------------------------

print("\n4. LOGARITHMIC FUNCTION")

f3 = log(x)

print("Function:")
print("ln(x)")

print("\nDerivative:")
print(diff(f3, x))

# --------------------------------------------------
# Example 5: Trigonometric Functions
# --------------------------------------------------

print("\n5. TRIGONOMETRIC FUNCTIONS")

print("Derivative of sin(x):")
print(diff(sin(x), x))

print("\nDerivative of cos(x):")
print(diff(cos(x), x))

print("\nDerivative of tan(x):")
print(diff(tan(x), x))

# --------------------------------------------------
# Example 6: Evaluation at a Point
# --------------------------------------------------

print("\n6. DERIVATIVE AT A SPECIFIC POINT")

f4 = x**2

derivative_f4 = diff(f4, x)

print("Function:")
print(f4)

print("Derivative:")
print(derivative_f4)

print("\nDerivative at x = 3")

value = derivative_f4.subs(x, 3)

print(value)

# --------------------------------------------------
# Example 7: Machine Learning Connection
# --------------------------------------------------

print("\n7. MACHINE LEARNING EXAMPLE")

loss_function = x**2 + 4*x + 3

print("Loss Function:")
print(loss_function)

gradient = diff(loss_function, x)

print("\nGradient (Derivative):")
print(gradient)

# --------------------------------------------------
# End
# --------------------------------------------------

print("\n" + "=" * 50)
print("PROGRAM EXECUTED SUCCESSFULLY")
print("=" * 50)
