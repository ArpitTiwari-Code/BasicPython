#WAP for creating a student marks profile with marks of 5 subjects
name= (input("name  of the student"))
Class=(input("class of student"))
maths=int(input("enter the marks of maths "))
english=int(input("enter the marks of english "))
physics=int(input("enter the marks of physics "))
chemistry=int(input("enter the marks of chemistry  "))
computer_science=int(input("enter the marks of computer_science"))
total_marks=chemistry+computer_science+physics+english+maths
print("total marks of all 5 subjects =",total_marks)
out_of_marks=500
percentage=(total_marks/out_of_marks)*100
print("percentage of student in all 5 subject =",percentage)
