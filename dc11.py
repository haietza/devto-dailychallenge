# https://dev.to/thepracticaldev/daily-challenge-11-cubic-numbers-21am

import sys
import math

def main(string):
    instring = False
    digitstr = ''
    strs = []
    for i in range(len(string)):
        if string[i].isdigit():
            instring = True
            digitstr += string[i] 
        else:
            instring = False
        if (not instring or i == len(string) - 1) and len(digitstr) > 0:
            strs.append(digitstr)
            digitstr = ''
    getcubics(strs)

def getcubics(strs):
    newstrs = []
    for number in strs:
        if len(number) > 3:
            numstrs = len(number) / 3
            count = 0
            i = 0
            while count < numstrs:
                newstrs.append(number[i] + number[i + 1] + number[i + 2])
                count += 1
                i += 3
            if count < numstrs:
                left = len(number) % 3
                count = 0
                while count < left:
                    newstrs.append(number[i])
                    count += 1
                    i += 1
        else:
            newstrs.append(number)

    answer = ''
    for newstr in newstrs:
        total = 0
        for num in newstr:
            total += math.pow(int(num), 3)
        if total == int(newstr):
            answer += newstr + ' '
    
    if len(answer) > 0:
        print(answer)
    else:
        print("Unlucky")

main(sys.argv[1])
