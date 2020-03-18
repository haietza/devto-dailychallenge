# Your goal is to create a function that removes the first and last letters of a string. Strings with two characters or less are considered invalid. You can choose to have your function return null or simply ignore. 

# Get string passed as command line argument.
import sys

string = sys.argv[1]
print("Original string: " + string)
strlen = len(string)
if strlen > 2:
    end = strlen - 1
    peeledstr = string[1:end]
    print("Peeled string: " + peeledstr)
else:
    print("Strings with two characters or less are invalid.")