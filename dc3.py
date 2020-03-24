# Write a function that returns the number (count) of vowels in a given string. 
# Letters considered as vowels are: a, i, e, o, and u. 
# The function should be able to take all types of characters as input, including lower case letters, upper case letters, symbols, and numbers. 

# Get command line argument.
import sys

def isvowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char.lower() in vowels:
        return True
    else:
        return False

def countvowels(string):
    count = 0
    for x in string:
        if isvowel(x):
            count+=1
    print(count)

countvowels(sys.argv[1])
