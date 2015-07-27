import random

symbols = ['rock', 'paper', 'scissors']

player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:
    player_symbol = None
    while player_symbol is None:
        input_symbol = raw_input("\nWhat symbol would you like to play? ")
        if input_symbol in symbols:
            player_symbol = input_symbol
        else:
            print "\nPlease pick from these symbols: rock, paper, scissors"

    computer_symbol = random.choice(symbols)

    print
    print "Player:   ", player_symbol
    print "Computer: ", computer_symbol
    print

    if player_symbol == computer_symbol:
        print "TIE!"
    elif player_symbol == 'rock':
        if computer_symbol == 'paper':
            print 'COMPUTER WINS!'
            computer_wins += 1
        else:
            print 'PLAYER WINS!'
            player_wins += 1
    elif player_symbol == 'paper':
        if computer_symbol == 'scissors':
            print 'COMPUTER WINS!'
            computer_wins += 1
        else:
            print 'PLAYER WINS!'
            player_wins += 1
    else:
        if computer_symbol == 'rock':
            print 'COMPUTER WINS!'
            computer_wins += 1
        else:
            print 'PLAYER WINS!'
            player_wins += 1

    print
    print "Player Wins:   ", player_wins
    print "Computer Wins: ", computer_wins
    print
