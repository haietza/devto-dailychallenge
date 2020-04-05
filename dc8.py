# https://dev.to/thepracticaldev/daily-challenge-8-scrabble-word-calculator-41f6

import sys

letterscores = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1,
    'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

def calculatescore(word):
    word = word.upper()
    score = 0;
    wordmultiplier = 1
    if word[len(word) - 1] == ')':
        if word[len(word) - 2] == 'D':
            wordmultiplier = 2
        elif word[len(word) - 2] == 'T':
            wordmultiplier = 3 
        word = word[:-3]
    wordlen = len(word)

    i = 0
    end = wordlen

    while i < end: 
        if i + 1 < len(word) and word[i + 1] == '*':
            # Possible double or triple, check for * and blank.
            if i + 2 < len(word) and word[i + 2] == '*':
                # Possible triple, check for blank.
                if i + 3 < len(word) and word[i + 3] != '^':
                    # Triple letter, add score.
                    score += letterscores[word[i]] * 3
                    # Advance past two *.
                    i += 2 
                    wordlen -= 2
                else:
                    # Blank, no score, but advance index past two * and ^.
                    i += 3 
                    wordlen -= 3
            else:
                # Possible double, check for blank.
                if i + 2 < len(word) and word[i + 2] != '^':
                    # Double letter, add score.
                    score += letterscores[word[i]] * 2
                    # Advance past one *.
                    i += 1
                    wordlen -= 1
                else:
                    # Blank, no score, but advance index past one * and ^.
                    i += 2 
                    wordlen -= 2
        else:
            # Possible regular letter, check for blank.
            if i + 1 < len(word) and word[i + 1] == '^':
                # Blank, no score, but advance index past ^.
                i += 1
                wordlen -= 1
            else:
                # Regular letter, add score.
                score += letterscores[word[i]]
        # Advance while loop.
        i += 1

    score *= wordmultiplier
    if wordlen > 6:
        score += 50
    print("Your score is: " + str(score))

calculatescore(sys.argv[1])
