first = input('Enter your first string: ')
second = input('Enter your second string: ')

if first != '' and second != '' :
    command = input('Enter your command: ')
    if command == 'find' :
        print(second in first)

    elif command == 'concat' :
        print(f'Your string is: {first + " " + second}')

    elif command == 'beatbox' :
        fint = int(input('Enter your first beatbox number: '))
        sint = int(input('Enter your second beatbox number: '))
        print(f'{first * fint + second * sint}')

    else : print ('usage: command find | concat | beatbox')
else : print('One of the strings is empty.')