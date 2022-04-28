
way = input('There are 3 signs in front of you. Which one would you like to read? ')
#way = str(way)

if way == 'right' :
    print(f'The {way} sign says: "DEAD PEOPLE ONLY"')
elif way == 'left' :
    print(f'The {way} sign says: "BEWARE!"')
elif way == 'middle' :
    print(f'The {way} sign says: "CERTAIN DEATH"')
else : 
    print(f'There is no {way} sign')
