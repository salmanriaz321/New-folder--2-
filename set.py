def setornot(number,s):
    if number &(1<<(s-1)):
        print("set")
    else:
        print("not set")
s=int(input("enter a number"))
r=int(input("enter a number"))
setornot(s,r)
