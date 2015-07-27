import random

symbols = ['rock', 'paper', 'scissors']

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
    else:
        print 'PLAYER WINS!'
elif player_symbol == 'paper':
    if computer_symbol == 'scissors':
        print 'COMPUTER WINS!'
    else:
        print 'PLAYER WINS!'
else:
    if computer_symbol == 'rock':
        print 'COMPUTER WINS!'
    else:
        print 'PLAYER WINS!'
