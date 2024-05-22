#wap to entr str and count no of : alpha, caps letter, small letter, digit, spaces
st=input("enter the str")
u=0
l=0
d=0
s=0
for i in st:
    if i.isupper ():
        u=u+1
        print = ("no of caps:",u)
    elif i.lower():
        l=l+1
        print = ("no of lower case:",l)
    elif i.isdigit():
        d=d+1
        print = ("no of digit:",d)
    elif i.isspace():
        s=s+1
        print = ("no of spaces:",s)
