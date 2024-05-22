a=eval(input("enter the list"))
b=input("enter what you want replace")
c=input("what you want to replace with")
for i in a:     
    print(i)
    if i == b:
        a[i]=c
        
print(a)
    
