import random
# Please note: This program was only tested using Python 2.7
def main():
        userGuess = input("I will flip a coin 1000 times. Enter your guess on how many flips will result in heads:  ")
        flips = 0
        heads = 0
        while (flips < 1000):
                if (random.randint(0, 1) == 1):
                        heads += 1
                flips += 1

                if (flips % 250 == 0 and flips != 1000):
                        print("At %d there were %d head results!" % (flips, heads))
        difference = (int(userGuess) - int(heads))
        print('\nOut of 1000 coin tosses, heads came up '+str(heads)+' times!')
        print('Your guess was '+str(difference)+' away from the result! Well done!')
main()
