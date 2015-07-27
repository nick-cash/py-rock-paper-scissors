import random

symbols = ['rock', 'paper', 'scissors']

player_symbol = raw_input("\nWhat symbol would you like to play? ")
computer_symbol = random.choice(symbols)

print
print 'Player:   ', player_symbol
print 'Computer: ', computer_symbol
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
elif player_symbol == 'scissors':
    if computer_symbol == 'rock':
        print 'COMPUTER WINS!'
    else:
        print 'PLAYER WINS!'
else:
    print 'Unsure what to do about symbol: ' + player_symbol
