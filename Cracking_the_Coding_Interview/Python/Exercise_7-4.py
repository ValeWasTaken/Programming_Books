# Write methods to implement the subtract, multiply, and divide  operations for integers using only the add operator.
# Python 3.4
    
def subtract(number1, number2):
    if number2 > 0:
        answer = number1 + (~number2 + 1)
    else:
        answer = number1 + (~~number2)
    print("{0} - {1} = {2}".format(number1,number2,answer))
    
def multiply(number1, number2):
    answer = 0
    for x in range(number2):
        answer += number1
    print("{0} * {1} = {2}".format(number1,number2,answer))
    
def divide(number1, number2):
    temp, answer = 0, 0
    while(temp < number1):
        answer += 1
        temp += number2
    print("{0} / {1} = {2}".format(number1,number2,answer))

def main():
    number1 = int(input())
    number2 = int(input())

    subtract(number1, number2)
    multiply(number1, number2)
    divide(number1, number2)
main()
