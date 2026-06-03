def is_prime(n):
    # Prime numbers must be greater than 1
    if n < 2:
        return False
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Iterate through all two-digit numbers (10 to 99)
primes_2_digit = [num for num in range(10, 100) if is_prime(num)]

print("Two-digit prime numbers are:")
print(primes_2_digit)

