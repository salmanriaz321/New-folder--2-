n = 10
r = 7
print("===Bitplay 3===")
print("Brfore n=", n, "r=", r)
n = n+r
r = n-r
n = n-r
print("Swapped: n=", n, "r=", r)
print()
n = 10
r = 7
n = n^r
r = n^r
n = n^r
print("XOR swap: n=", n, "r=", r)
print()
print("Left shift:")
print("  3 << 1 =", 3 << 1)
print("  3 << 2 =", 3 << 2)
print("  3 << 3 =", 3 << 3)
print("  3 << 4 =", 3 << 4)
print("  3 << 5 =", 3 << 5)
print()
def divide(a, b):
    negative = (a < 0) ^ (b < 0)
    a = abs(a)
    b = abs(b)
    count = 0
    while a >=b:
        a = a-b
        count = count+1
    if negative:
        count = -count
    return count
print("divide without /:")
print(" 50 / 2 =", divide(50,2))
print(" 72 / 3 =", divide(72,3))
print(" -50 / 2 =" , divide(-50,2))
print(" 50 / -2 =", divide(50,-2))
