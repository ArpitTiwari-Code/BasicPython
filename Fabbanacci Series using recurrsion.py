"""Fabbanacci Series using recurrsion
"""
def feb(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n>= 2:
        return (feb(n-1) + feb( n-2))
n=int(input("enter the num"))
for i in range(1,n+1):
    print(feb(i))
