def powerof4(s):
    count=0
    if((s & (~(s-1)))):
        while(s>1):
            s>>=1
            count+=1
        if count% 2==0:
            return True
        else:
            return False
number=int(input("enter a number"))
if( powerof4(number)):
    print("Number is power of 4")
else:
    print("Number is not power of 4")