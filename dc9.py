# https://dev.to/thepracticaldev/daily-challenge-9-what-s-your-number-3707

import sys

def getphone(numbers):
    if len(numbers) > 10 or len(numbers) < 10:
        print("Need 10 numbers to get phone")
        exit()
    phone = '('
    for number in numbers[:3]:
        phone += number
    phone += ') ' 
    for number in numbers[3:6]:
        phone += number
    phone += '-'
    for number in numbers[6:]:
        phone += number
    print(phone)

getphone(sys.argv[1])
