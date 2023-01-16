import random as rnd

def game():
    playerscore = 0
    computerscore = 0
    player1 = ''
    answerslist = ['rock','paper','scissors']
    print('please choose r for rock, p for paper and s for scissors')
    print('-'*70)
    while (i := input('rock paper scissors... : ')) != 'exit':
        
        computeranswer = answerslist[rnd.randint(0,2)]

        if i == 'r':
            if computeranswer == 'rock':
                print(computeranswer)
                pass
            elif computeranswer == 'paper':
                print(computeranswer)
                computerscore += 1
            else:
                print(computeranswer)
                playerscore += 1
        elif i == 'p':
            if computeranswer == 'rock':
                print(computeranswer)
                playerscore += 1
            elif computeranswer == 'paper':
                print(computeranswer)
                pass
            else:
                print(computeranswer)
                computerscore += 1
        elif i =='s':
            if computeranswer == 'rock':
                print(computeranswer)
                computerscore += 1
            elif computeranswer == 'paper':
                print(computeranswer)
                playerscore += 1
            else:
                print(computeranswer)
                pass
        else:
            print('please input r,p or s! ')
    
    print('-'*70)
    if computerscore == playerscore:
        print(f'Its a tie! Your score is : {playerscore} and Computerscore is : {computerscore}')
    elif computerscore < playerscore:
        print(f'You won! Your score is : {playerscore} and Computerscore is : {computerscore}')
    else:
        print(f'You lost! Your score is : {playerscore} and Computerscore is : {computerscore}')


if __name__ == "__main__":

    game()

