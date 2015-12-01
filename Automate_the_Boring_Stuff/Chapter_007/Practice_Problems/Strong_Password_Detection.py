# Chapter 7: Strong Password Detection - Python 3.4
import re

def is_password_strong():
    """
    Returns a boolean indicating if the password is strong.

    Strong passwords are defined here as 8 characters or longer,
    contain at least one uppercase letter,
    lowercase letter and digit.
    """
    password = input('Enter a password to test: ')
    
    length_regex = re.compile(r'.{8,}')
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')
    
    length = length_regex.search(password) is not None
    case = (uppercase_regex.search(password) is not None and
        lowercase_regex.search(password) is not None)
    digit = digit_regex.search(password) is not None

    return(length and case and digit)
