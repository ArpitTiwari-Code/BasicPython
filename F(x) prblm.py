a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
d=int(input("enter the value of d"))
x=int(input("enter the value of x"))
k=int(input("enter the value of k"))

if x>k:
    print("F(x)=",a*x**2-b*x**3+c*x-d)
elif x==k:
    print("F(x)=",0)
else:
    print("F(x)=",-a*x**3+b*x**2-c*x+d)
