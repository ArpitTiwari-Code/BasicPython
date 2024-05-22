#wap to write a program of n==L[i]
l=eval(input("enter the list"))
n=int(input("enter the element"))
for i in range(len(l)):
    if l[i]==n:
        print("element found in index",i)
        print("no. of times it is repeated",l.count(n))
        print()
else:
    print ("not found")
