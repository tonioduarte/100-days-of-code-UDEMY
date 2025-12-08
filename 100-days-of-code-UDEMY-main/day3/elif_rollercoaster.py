print ('welcome to the rollercoaster')
height = int(input(' what is your height in cm? '))

if height >= 120:
    print(' you can ride! ')
    age = int(input( ' what is your age? '))
    photo = input(' you want photos? it will include 3$ at your ticket ')
    if age <= 12:
        if photo == 'yes':
            print(' your ticket is now 9$')
        else:
            print(' your ticket is 6$ ')
    elif age <= 18:
        if photo == 'yes':
            print(' your ticket is now 11$ ')
        else: 
            print(' your ticket is 8$ ')
    elif age >= 45 and age < 55: #A and B: os 2 precisam ser TRUE, or = 2 precisam ser FALSE, not E = tem q ser falsopir
        if photo == 'yes':
            print(' your ticket has a discount and is now 10$ ')
        else: 
            print(' your ticket has a discount and is now 8$ ')
    else:
        if photo == 'yes':
            print(' your ticket is now 15$ ')
        else: 
            print(' your ticket is 12$ ')
else: 
    print(' you cant ride :( ')