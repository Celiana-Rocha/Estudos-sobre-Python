from random import randint

N = 0
scott = 0
ben = 0
scott_is = 3
ben_is = 9

while N < 5:
    choice_scott = randint(1, 10)
    choice_ben = randint(1, 10)

    if choice_ben == ben_is:
        print('Point for Ben!!')
        ben += 1 
    
    elif choice_scott == scott_is:
        print('Point for Scott!!')
        scott += 1

    N += 1

print(f'''
        scoreboard
    Ben: {ben}
    scott: {scott}      
    ''')