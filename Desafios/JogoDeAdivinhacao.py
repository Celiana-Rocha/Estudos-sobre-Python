from random import randint

Pc = randint(1, 10)
player = 0
allempt = 0

while allempt < 10:
    print('NEW GAME')
    
    player = int(input('What number do you want to guess? \n --> '))
    
    if player == Pc:
        print('Player win!!')
        print(f'''
            your number: {player}
            number of Pc: {Pc}                    
        ''')
        break

    else:
        print('Pc win! player was lost :(')
        print(f'number of Pc: {Pc}')
        allempt += 1

print(f'allempt number:{allempt}')