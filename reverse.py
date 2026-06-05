def reverse_4bits(n):
    return int(f"{n:04b}"[::-1], 2)

# Test cases
for num in [12, 11]:
    print(f"Original: {num} -> Reversed: {reverse_4bits(num)}")
