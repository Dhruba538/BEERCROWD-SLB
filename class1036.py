import math

# Read three floating-point numbers
A, B, C = map(float, input().split())

# Calculate the discriminant
D = B**2 - 4*A*C

# Check for impossible calculations
if A == 0 or D < 0:
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(D)) / (2 * A)
    R2 = (-B - math.sqrt(D)) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
