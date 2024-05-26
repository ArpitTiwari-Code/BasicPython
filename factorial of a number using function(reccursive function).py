#factorial of a number using function(reccursive function)

def factorial(no):
    if (no==0 or no==1):
        return(1)
    else:
        return(no * factorial(no-1))
no=int(input("enter the no"))
a=factorial(no)
print(a)
