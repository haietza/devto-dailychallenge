# Your goal is to create a function that removes the first and last letters of a string. Strings with two characters or less are considered invalid. You can choose to have your function return null or simply ignore. 
# Your task is to return a string that displays a diamond shape on the screen using asterisk ("*") characters.
# The shape that the print method will return should resemble a diamond. A number provided as input will represent the number of asterisks printed on the middle line. The line above and below will be centered and will have two less asterisks than the middle line. This reduction will continue for each line until a line with a single asterisk is printed at the top and bottom of the figure.
# Return null if input is an even number or a negative number.
# Note: JS and Python students must implement diamond() method and return None (Py) or null(JS) for invalid input.

# Get command line argument.
import sys

def printspaces(num):
    for x in range(num):
        sys.stdout.write(" ")

def printstars(num):
    for x in range(num):
        sys.stdout.write("*")

def diamond(numstars):
    numstars = int(numstars)
    if numstars < 0 or numstars % 2 == 0:
        return None

    numlines = numstars / 2
    numspaces = numlines
    prntstars = 1

    # Print lines leading up to full line.
    for x in range(numlines):
        printspaces(numspaces)
        printstars(prntstars)
        print("")
    
        numspaces-=1
        prntstars+=2

    # Print full line.
    printspaces(numspaces)
    printstars(prntstars)
    print("")

    numspaces+=1
    prntstars-=2

    # Print lines following full line.
    for x in range(numlines - 1):
        printspaces(numspaces)
        printstars(prntstars)
        print("")

        numspaces+=1
        prntstars-=2

    # Print last line.
    printspaces(numspaces)
    printstars(prntstars)

diamond(sys.argv[1])
