# https://dev.to/thepracticaldev/daily-challenge-4-checkbook-balancing-hei

import sys
import re

def cleanlines(string):
    lines = string.split('\\n')
    newlines = []
    for line in lines:
        newlines.append(re.sub(r'[^\s\d\.a-zA-Z]*', '', line))
    return newlines 

def getamounts(lines):
    amounts = []
    for line in lines[1:]:
        words = line.split(" ")
        amounts.append(float(words[2]))
    return amounts

def gettotal(amounts):
    total = 0
    for amount in amounts:
        total += amount
    return total

def getbalances(amounts, original):
    balances = []
    subtotal = original 
    for amount in amounts:
        subtotal -= amount 
        balances.append(subtotal)
    return balances

def getlines(lines):
    newlines = []
    for line in lines[1:]:
        words = line.split(" ")
        newlines.append(words[0] + " " + words[1])
    return newlines

def printsolution(original, amounts, balances, lines):
    print("Original_Balance: {:.2f}".format(original))
    for (line, amount, balance) in zip(lines, amounts, balances):
        newline = line + " {:.2f} Balance {:.2f}"
        print(newline.format(amount, balance))
    total = gettotal(amounts)
    print("Total expense {:.2f}".format(total))
    average = total / len(amounts)
    print("Average expense {:.2f}".format(average))

def main(string):
    lines = cleanlines(string)
    originalbalance = float(lines[0])
    amounts = getamounts(lines)
    balances = getbalances(amounts, originalbalance)
    newlines = getlines(lines)
    printsolution(originalbalance, amounts, balances, newlines)

main(sys.argv[1])
