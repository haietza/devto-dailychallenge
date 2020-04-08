# https://dev.to/thepracticaldev/daily-challenge-9-what-s-your-number-3707

import sys

def calculate(expression):
    elements = expression.split()
    mdindices = [i for i, x in enumerate(elements) if x == '*' or x == '/']
    newexp = []
    cursor = 0
    end = len(elements)
    while cursor < end:
        if cursor + 1 in mdindices:
            if elements[cursor + 1] == '*':
                newexp.append(int(elements[cursor]) * int(elements[cursor + 2]))
            elif elements[cursor + 1] == '/':
                newexp.append(int(elements[cursor]) / int(elements[cursor + 2]))
            cursor += 3
        else:
            newexp.append(elements[cursor])
            cursor += 1

    cursor = 1
    end = len(newexp)
    value = newexp[0] 
    while cursor < end:
        if newexp[cursor] == '+':
            value += int(newexp[cursor + 1])
        else:
            value -= int(newexp[cursor + 1])
        cursor += 2
    print(value)

calculate(sys.argv[1])
