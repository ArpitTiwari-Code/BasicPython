#wap to check no is in or not if in whts the position
l=eval(input("enter the list"))
n=int (input("entr the no"))
for i in range (len(l)):
    if l[i]==n:
        print("no is in the list")
        print("index val of give no.",l[i])
        break
else:
         print("not in")
