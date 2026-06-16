# ------------------------------------------------
# PART 5 — BINARY EXPONENTIATION
# ------------------------------------------------
def binary_exponentiation(base, exp):
    result = 1
    current_product = base
    
    while exp > 0:
        # If the lowest bit of the exponent is 1, multiply the result by current_product
        if exp & 1:
            result *= current_product
        
        # Square the base for the next bit position
        current_product *= current_product
        
        # Shift right to process the next bit of the exponent
        exp >>= 1
        
    return result

print("PART 5: Binary Exponentiation")
test_cases = [(2, 10), (3, 5), (5, 4)]

for base, exp in test_cases:
    print(f"{base}^{exp} -> {binary_exponentiation(base, exp)}")
