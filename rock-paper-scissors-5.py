import random

symbols = ['rock', 'paper', 'scissors']

player_wins = 0
computer_wins = 0

while max([player_wins, computer_wins]) < 3:
    player_symbol = None
    while player_symbol is None:
        input_symbol = raw_input("\nWhat symbol would you like to play? ")
        if input_symbol in symbols:
            player_symbol = input_symbol
        else:
            print "\nPlease pick from these symbols: rock, paper, scissors"

    computer_symbol = random.choice(symbols)

    print "\nPlayer:   " + player_symbol
    print "Computer: " + computer_symbol + '\n'

    if player_symbol == computer_symbol:
        print "TIE!"
    elif ((player_symbol == 'rock' and computer_symbol == 'paper') or
          (player_symbol == 'paper' and computer_symbol == 'scissors') or
          (player_symbol == 'scissors' and computer_symbol == 'rock')):
        computer_wins += 1
        print 'COMPUTER WINS!'
    else:
        player_wins += 1
        print 'PLAYER WINS!'

    print "\nPlayer Wins:   ", player_wins
    print "Computer Wins: ", computer_wins, '\n'
