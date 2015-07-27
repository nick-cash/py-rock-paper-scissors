import random

symbols = ['rock', 'paper', 'scissors']

player_symbol = raw_input("\nWhat symbol would you like to play? ")
computer_symbol = random.choice(symbols)

print
print 'Player:   ', player_symbol
print 'Computer: ', computer_symbol
print
