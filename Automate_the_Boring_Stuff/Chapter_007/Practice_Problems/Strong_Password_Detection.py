def is_password_strong():
    password = input('Enter a password to test: ')
    
    length_regex = re.compile(r'.{8,}')
    length = True if length_regex.search(password) != None else False

    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    uppercase = True if uppercase_regex.search(password) != None else False
    lowercase = True if lowercase_regex.search(password) != None else False
    case = True if uppercase and lowercase == True else False

    digit_regex = re.compile(r'[0-9]')
    digit = True if digit_regex.search(password) != None else False

    return(length and case and digit == True
print(is_password_strong())
