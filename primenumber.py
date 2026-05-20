from math import sqrt
number=int(input("enter a number"))
if number >0:
    for i in range(2,int(sqrt(number))+1):
        if (number%i)==0:
            print("is not a prime number")
            break
    else:
        print("it is a prime number")
else:
    print("not a prime number")
    