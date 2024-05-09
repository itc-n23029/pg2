import random
import sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        
        if player_move == 'q':
            sys.exit()
        elif player_move in ['r', 'p', 's']:
            break
        else:
            print('Type one of r, p, s, or q.')

    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    random_number = random.randint(1, 3)
    
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1

