# write a program to calc. sum of n no. of natural no
n=int(input("enter the no the calc. sum of n no. of natural no "))
no=1
if n==0:
    print("0 is not a natural no.")
   
else:
    for i in range (1,n) :
       no= i + no
print("sum of ",n,"no. of natural no",no)    
