def collatz(number):
    try:
        number = int(number) # Doing this because Python 3 input() != a number by default. Also to catch ValueErrors.
        while number != 1:
            if number % 2 == 0:
                number //= 2
            elif number % 2 != 0:
                number = (3*number) + 1
            print(number)
    except ValueError:
        print("You must enter an integer.")
collatz(input())
