import math

# Get inputs
num1 = 20
num2 = 80

# Calculate LCM using math.gcd (requires Python 3.9+)
lcm = abs(num1 * num2) // math.gcd(num1, num2)

print(f"Largest number: {num1}")
print(f"Smallest number: {num2}")
print(f"LCM is: {lcm}")
