#wap to create basic salary of a person
employee_name=input("enter the name of employy")
annual_inc=float(input("enter the salary of abv employy"))
if annual_inc>=60000:
    i=annual_inc/100*8
    salary=annual_inc-i
elif annual_inc >=30000 and annual_inc < 60000:
    i=annual_inc/100*6
    salary=annual_inc-i
elif annual_inc >= 15000 and annual_inc < 30000:
    i =annual_inc/100*2
    salary=annual_inc-i
else:
    i=annual_inc/100*0
    salary=annual_inc-i
print(salary)
