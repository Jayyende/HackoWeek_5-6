# chain_rule.py

print("=" * 50)
print("CHAIN RULE IN CALCULUS")
print("=" * 50)

# Example:
# y = (x² + 1)³

def outer_derivative(u):
    return 3 * (u ** 2)

def inner_derivative(x):
    return 2 * x

x = 2

u = x**2 + 1

chain_rule_result = outer_derivative(u) * inner_derivative(x)

print("\nFunction:")
print("y = (x² + 1)³")

print("\nValue of x:")
print(x)

print("\nValue of Inner Function:")
print(u)

print("\nDerivative using Chain Rule:")
print(chain_rule_result)

print("\nExplanation:")
print("Outer Derivative × Inner Derivative")

print("\n" + "=" * 50)
print("PROGRAM EXECUTED SUCCESSFULLY")
print("=" * 50)
