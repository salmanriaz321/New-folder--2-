def oddoreven(arr):
    rest=0
    for element in arr:
        rest=rest^element
    return rest
arr=[]
r=int(input("enter array size"))
while(r):
    num=int(input("enter a number"))
    arr.append(num)
    r-=1
print("odd occurring number", oddoreven(arr))
