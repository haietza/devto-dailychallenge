# https://dev.to/thepracticaldev/daily-challenge-11-cubic-numbers-21am

import sys
import math

def main(number):
    if len(number) <= 3:
        sum = 0
        for num in number:
            sum += math.pow(int(num), 3)
        if sum == int(number):
            print("Cubic number")
            exit()
    print("Unlucky")

main(sys.argv[1])
