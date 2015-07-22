# Python 3.4 - Interview Question 1.3
# Given two strings,
# write a method to decide if one is a permutation of the other. 
from collections import Counter

def is_permutation(string1,string2):
    string1_count = Counter([x for x in string1[::]])
    string2_count = Counter([x for x in string2[::]])
    if string1_count == string2_count:
        print("Strings are permutations of each other.")
    else:
        print("Strings are not permutations of each other.")
is_permutation(input(),input())
