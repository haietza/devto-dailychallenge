# https://dev.to/thepracticaldev/daily-challenge-6-grandma-and-her-friends-23kd
# https://www.codewars.com/kata/help-your-granny/javascript

import math

friends = ['A1', 'A2', 'A3', 'A4', 'A5']
addresses = {'A1': 'X1', 'A2': 'X2', 'A3': 'X3', 'A4': 'X4', 'A5': 'X5'}
distances = {'X1': 100.0, 'X2': 200.0, 'X3': 250.0, 'X4': 300.0, 'X5': 350.00}

def getpath():
    path = []
    for friend in friends:
        path.append(addresses[friend])
    return path

def calculatedistance(address1, address2):
    a = distances[address1]
    a2 = a**2
    c = distances[address2]
    c2 = c**2
    b2 = c2 - a2
    b = math.sqrt(b2)
    print("distance from {0} to {1} is {2}".format(address1, address2, b))
    return b

def gettotalmiles():
    path = getpath()
    totaldistance = distances[path[0]] 
    print("distance from {0} to {1} is {2}".format("X0", path[0], totaldistance))
    for address in path[:-1]:
        nextindex = path.index(address) + 1
        totaldistance += calculatedistance(address, path[nextindex])
    totaldistance += distances[path[-1]]
    print("distance from {0} back to {1} is {2}".format(path[-1], "X0", distances[path[-1]]))
    print("total distance to travel for path ")
    print(path)
    print(totaldistance)

gettotalmiles()
