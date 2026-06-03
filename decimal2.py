def binary_to_decimal():
    # Prompt the user for a binary string
    binary_str = input("Enter your Binary: ")
    
    try:
        # int(string, base) converts base-2 to base-10
        decimal_val = int(binary_str, 2)
        print(f"Decimal : {decimal_val}")
    except ValueError:
        print("Invalid binary input. Please enter only 0s and 1s.")

binary_to_decimal()
