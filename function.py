def e(n):
    if (n ^1==n+1):
        return True;
    else:
        return False;
number=int(input("enter a number"))
if e(number):
    print("Even number")
else:
    print("Odd number")
    