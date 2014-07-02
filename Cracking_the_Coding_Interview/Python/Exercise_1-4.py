# Replace spaces with "%20"
# Ex: "Hello world" -> "Hello%20world"

def replace_spaces(input):
    message = ''
    for letter in input:
        if(letter == ' '):
            message += "%20"
        else:
            message += letter
    print(message)

def main():
    message = raw_input("Input message: ")
    replace_spaces(message)
main()
