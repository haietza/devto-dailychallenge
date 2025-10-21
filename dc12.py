# https://dev.to/thepracticaldev/daily-challenge-12-next-larger-number-3f3o

import sys
import math

def main(string):
    digits = string.split();
    sortpoint = findsortpoint(digits);
    swap = findnextlargest(sortpoint, digits);



def findsortpoint(digits):
    found = False;
    i = 1;
    while not found and i < len(digits):
        if digits[i] < digits[i - 1]:
            found = True;
        i += 1;
    return i



def findnextlargest(i, digits):
    swap = 10;
    for j in range(i + 1, len(digits)):
        if digits[j] > digits[i] and digits[j] < swap:
            swap = digits[j];
    return swap;

main(sys.argv[1])
