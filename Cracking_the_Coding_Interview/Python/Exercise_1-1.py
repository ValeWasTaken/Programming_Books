# Implement an algorithm to determine if a string has all unique characters.
# Python 3.4 - Change to Python 2.7 by modifying input() to raw_input()

def is_unique(string):
    unique_characters = []  # Stores characters we will be reading one by one.
    for char in string[::]: # [::] Splits string into individual characters.
        if char not in unique_characters:
            unique_characters.append(char)
        else:
            return False
    return True # If no characters returned False (non-unique) return True.

def main():
    if is_unique(input()) == True:
        print("String contains all unique characters.")
    else:
        print("String does NOT contain all unique characters.")

main()
