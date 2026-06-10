def powerofnumbers (m):
    if m==0:
        return 0
    if((m & (~(m-1)))==m):
        return 1
    return 0
number=int(input("enter a number"))
if(powerofnumbers(number)):
    print("number is power of 2")
else:
    print("number is not power of 2")
