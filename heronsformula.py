import math
a=int(input("enter side"))
b=int(input("enter side"))
c=int(input("enter side"))

C= a+b+c
s=C/2


area= math.sqrt(s*(s-c)*(s-a)*(s-b))

print(area,"msq.")
