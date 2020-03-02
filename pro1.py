print("welcome to the Even-Odd Gmae ")
print("please enter a number .... and i will tell you if it Even or Odd")
while True :

    number = input("enter the number : ")
    if number == 'x':
              print('closing the  game')
              print('thanks...')
              break
              
       
        
    try :
        number = int(number)
        if number % 2 == 0 :
            print("even nomber ")

        else:
            print("odd number")
            
    except ValueError:
        print('please enter valid number')

    print('--------------------------')
