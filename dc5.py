# https://dev.to/thepracticaldev/daily-challenge-5-ten-minute-walk-1188

import sys
import random
from random import shuffle

def generatewalk(minutes):
    minutes = int(minutes)
    if minutes % 2 != 0 or minutes < 0:
        print "Minutes must be even in order for you to get back."
        sys.exit()

    directions = ['n', 's', 'e', 'w']
    path = []

    # Get first half of walk.
    for x in range(minutes / 2):
        randomint = random.randint(0, 3)
        path.append(directions[randomint])

    # Return to start.
    for x in range(minutes / 2):
        if path[x] == 'n':
            path.append('s')
        elif path[x] == 's':
            path.append('n')
        elif path[x] == 'e':
            path.append('w')
        elif path[x] == 'w':
            path.append('e')

    shuffle(path)
    print(path)
    
generatewalk(sys.argv[1])
