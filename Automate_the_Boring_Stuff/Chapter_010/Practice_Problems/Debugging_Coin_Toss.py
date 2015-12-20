import random

def play():
    guess = ''
    sides = ['heads','tails']
    while guess not in (sides):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input().lower()
    toss = random.choice(sides)
    
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        if toss == input().lower():
           print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
play()
