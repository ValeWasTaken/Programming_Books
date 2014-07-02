# Interview Questions - Exercise 6.5
# Imagine you have 2 eggs while at a 100 story building.
# If you drop an egg from the Nth floor or higher, it will break.
# Find the number, N, while minimizing the amount of drops.

# Side note: The books solution was going "14 + 13 + 12 + .." upwards to end with, at worst, 14 guesses.
# After running every form of incrementation 20,000 times each and averaging the amount of drops (given that the Nth floor is random each time)
# I found that incrementing by 10 (rounded to the nearest whole number) is the most efficient answer, with an average of approximately 11.9 guesses.
import random

def main():
    increment = 1
    while(increment < 101):
        
        attempt = 0
        guessTotal = 0
        while(attempt != 20000):
            dropEgg = True
            floor = 0
            nthFloor = 0
            guesses = 0
            targetFloor = random.randrange(1,100+1) #Assuming floor 1 is ground level
            eggs = 2

            while(dropEgg == True):
                if(eggs >= 2):
                    if(floor == targetFloor):
                        eggs = 0
                        guesses += 1
                    elif(floor > targetFloor):
                        eggs -= 1
                        guesses += 1
                    elif(floor < targetFloor):
                        floor += increment
                        guesses += 1
                    else: 
                        print("Error.1")
                        
                elif(eggs == 1):
                    if(floor == targetFloor):
                        eggs = 0
                        guesses += 1
                    elif(floor > targetFloor):
                        floor -= (increment + 1)
                    elif(floor < targetFloor):
                        floor += increment
                        guesses += 1
                    else:
                        print("Error.2")
                        
                elif(eggs == 0):
                    guessTotal += guesses
                    dropEgg = False
            attempt += 1
        guessAvg = (guessTotal / 20000.0)
        print("At increment %s the average amount of guesses was %s" % (increment, guessAvg))
        increment += 1
main()
