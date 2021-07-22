import random  # 引用module
win_game = 0;  # 初始值0 決定break條件==1
tie_game = 0;  # 初始值0
loss_game = 0  # 初始值0
print('Welcome to Rock,Paper,Scissors game!')
while win_game == 0:
    Playermove = input('Enter your move:(r)ock(p)aper(s)cissors')
    if Playermove == 'r':
        print('ROCK versus...')
    elif Playermove == 'p':
        print('Paper versus...')
    elif Playermove == 's':
        print('Scissors versus...')
    else:
        print('Error,please try it again.')
        break
    List = ['Rock', 'Paper', 'Scissors']
    Computermove = List[random.randint(0, 2)]  # 決定電腦的隨機出拳
    print(Computermove)
    if Playermove == 'r' and Computermove == 'Rock':
        print('It is a tie.')
        tie_game += 1
    elif Playermove == 'r' and Computermove == 'Paper':
        print('You loss!')
        loss_game += 1
    elif Playermove == 's' and Computermove == 'Scissors':
        print('It is a tie.')
        tie_game += 1
    elif Playermove == 's' and Computermove == 'Rock':
        print('You loss!')
        loss_game += 1
    elif Playermove == 'p' and Computermove == 'Paper':
        print('It is a tie.')
        tie_game += 1
    elif Playermove == 'p' and Computermove == 'Scisssors':
        print('You loss!')
        loss_game += 1
    else:
        print('You win!')
        win_game += 1
    if win_game == 1:
        print('You have', tie_game, 'ties and', loss_game, 'losses before you win.')
        break
    else:
        continue
