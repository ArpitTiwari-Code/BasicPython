 #to calculate days, hours, minutes, seconds from your birth
print("enter pass to unlock program")
print("PLEASE ENTER PASSWORD OF ONLY 4 DIGIT")
password=int(input('enter your password'))
print()
if password==7052:
          print("RIGHT PASSWORD!!,you enter the program")
          y=int(input('Enter the year: '))
          a=int(input('Enter the year of your birth: '))
          if a>y:
              print('this is impossible')
          elif y==a:
              print('bhai issi saal me hua he re tu')
          else:
              x=y-a
              d=365*x
              h=24*d
              m=60*h
              s=60*m
              print('years', x)
              print('days: ', d)
              print('hours: ', h)
              print('minutes: ', m)
              print('seconds: ',s)
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
                  y=int(input('Enter the year: '))
                  a=int(input('Enter the year of your birth: '))
                  if a>y:
                      print('this is impossible')
                  elif y==a:
                      print('bhai issi saal me hua he re tu')
                  else: 
                       x=y-a
                       d=365*x
                       h=24*d
                       m=60*h
                       s=60*m
                       print('years', x)
                       print('days: ', d)
                       print('hours: ', h)
                       print('minutes: ', m)
                       print('seconds: ',s)
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
            y=int(input('Enter the year: '))
            a=int(input('Enter the year of your birth: '))
            if a>y:
                   print('this is impossible')
            elif y==a:
                   print('bhai issi saal me hua he re tu')
            else: 
                    x=y-a
                    d=365*x
                    h=24*d
                    m=60*h
                    s=60*m
                    print('years', x)
                    print('days: ', d)
                    print('hours: ', h)
                    print('minutes: ', m)
                    print('seconds: ',s)
    else:
        print()     
    print('PLEASE TRY AFTER FEW SECONDS!!!')
    




    
    


