# Chapter 7: Regex Version of strip() - Python 3.4
import re

string = input("Enter a string to strip: ")
bad_chars = input("Enter the characters you want to be striped: ")

def regex_strip(string, bad_chars):
    """
    Replicates the usage of strip() utilizing regex.
    
    If no other arguments are passed other than the string to strip,
    then whitespace characters will be removed from the beginning
    and end of the string. Otherwise, the characters specified
    in the second argument to the function will be removed from the string.
    """
    strip_regex = re.compile('[%s]' % bad_chars)
    return strip_regex.sub('', string)
    
try:
    print(regex_strip(string, bad_chars))
except TypeError:
    print(regex_strip(string, ' '))
