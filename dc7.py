# https://dev.to/thepracticaldev/daily-challenge-7-factorial-decomposition-176o

import sys
import math

def getnextprime(prime):
    notprime = True
    while (notprime):
        prime += 1
        for x in range(2, prime):
            if prime % x != 0:
                notprime = False
    return prime

def decompose(n):
    nfactorial = math.factorial(int(n))
    prime = 2
    remainder = nfactorial
    answer = ''
    while prime <= remainder:
        exponent = 0
        while remainder % prime == 0:
            remainder /= prime
            exponent += 1
        if exponent == 1:
            answer += str(prime) + ' * '
        elif exponent > 1:
            answer += str(prime) + '^' + str(exponent) + ' * '
        prime = getnextprime(prime)
    answer = answer[:-3]
    print(answer)

decompose(sys.argv[1])
