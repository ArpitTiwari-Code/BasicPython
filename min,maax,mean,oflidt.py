#wap to find min, max,and mean
l=[2,4,5,6,7,7]
print("min value in a list is",min(l))
print("max value in a list is",max(l))
L=0
for i in range(len(l)):
    L=(L+l[i])
print(L/len(l))
n=int(input("enter the no. which is occured"))
print(l.count(n))
