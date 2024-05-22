#WAP to find greatest of 3 no
num1=float(input("enter the num1="))
num2=int(input("enter the num2="))
num3=int(input("enter the num3="))
if num1>num2 and num1>num3:
    print("num1 is the greatest")
    print(num1)
elif num2>num1 and num2>num3:
    print("num2 is greatest")
    print(num2)
elif num1==num2 and num1==num2>num3:
    print('num1 and num2 are greatest')
    print(num1,num2)
elif num2==num3 and num2==num3>num1:
    print('num2 and num3 are greatest')
    print(num2,num3)
elif num1==num3 and num1==num3>num2:
    print ('num1 and num3 are greatest')
    print(num1,num3)
else:
    print("num3 is greatest")
    print(num3)

