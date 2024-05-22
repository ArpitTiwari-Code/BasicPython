print("enter pass to unlock program")
print("PLEASE ENTER PASSWORD OF ONLY 4 DIGIT")
password=int(input('enter your password'))
print() 
if password==7052:
    print("RIGHT PASSWORD!!,you enter the program")
    print() 
else:
    for i in range (1,10):
        print("WRONG PASSWORD!!,enter password again")
        print() 
        np=int(input('enter your password'))
        print() 
        if np>0 :
               if np==7052:
                  print("you enter the program")
                  print() 
               else :
                   print("WRONG PASAWORD!!,enter password again")
                   print() 
        else:
            print()
        break    
    n_p=int(input('enter your password'))
    print() 
    if n_p>0 :
        if n_p==7052:
            print("you enter the program")
            print() 
    else:
        print()     
    print('PLEASE TRY AFTER FEW SECONDS!!!')
