def numbersofbits(n):
    ones=0
    zero=0
    while(n):
        if(n & 1==1):
            ones +=1
        else:
            zero +=1
        n>>=1
    print("ones =",ones,"zero =",zero)
number=int(input("enter a number"))
numbersofbits(number)
