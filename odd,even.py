def checkifsame(s,r):
    if((s^r)!=0):
        print("numbers are not equal")
    else:
        print("numbers are equal")
s=int(input("enter a number"))
r=int(input("enter a number"))
checkifsame(s,r)