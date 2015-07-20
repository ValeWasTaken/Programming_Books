# Python 3.4 - Interview Question 11.5
# Given an assorted array of strings which is intersperced with empty strings,
# write a method to find the location of a given string.

def main():
    array_of_strings = ['at','','','','ball','','','car','','','dad','','']
    given_string = input('Find location of string: ')
    for x in range(len(array_of_strings)):
        if array_of_strings[x] == given_string:
            print(x)
main()
