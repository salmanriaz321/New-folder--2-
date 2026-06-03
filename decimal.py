def binary_to_decimal(binary_str):
    decimal_value = 0
    # Reverse the string so we can process it from right to left
    binary_str = binary_str[::-1]
    
    for power, digit in enumerate(binary_str):
        if digit == '1':
            decimal_value += 2 ** power
            
    return decimal_value

# Test the exact examples you provided
print(binary_to_decimal("010"))   # Output: 2
print(binary_to_decimal("1101"))  # Output: 13
