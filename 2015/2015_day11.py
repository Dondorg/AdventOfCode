from AOC import *
from string import ascii_lowercase

def areConsecutiveLetters(first,second):
    if len(first) == 0 or len(second) == 0:
        return False
    return ord(second) - ord(first) == 1

def isValidPassword(pw):
    prePrevLetter = ""
    prevLetter = ""
    hasThreeConsecutiveLetters = False
    pairCount = 0
    pairs = {}
    for letter in pw:
        if letter in ["i","o","l"]:
            return False
        if letter == prevLetter:
            if not letter+letter in pairs:
                pairs[letter*2] = 1
                pairCount += 1
        if (areConsecutiveLetters(prePrevLetter,prevLetter) 
            and areConsecutiveLetters(prevLetter,letter)):
            hasThreeConsecutiveLetters = True
        
        prePrevLetter = prevLetter
        prevLetter = letter
    
    return hasThreeConsecutiveLetters and pairCount > 1

def incrementPassword(pw):
    pw = list(pw[::-1])
    for i in range(len(pw)):
        if pw[i] == "z":
             pw[i] = "a"
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break
    return ''.join(pw[::-1])

def solvePartOne():
    input = readInput(2015, 11)
    while (not isValidPassword(input)):
        input = incrementPassword(input)
    print(input)

def solvePartTwo():
    input = solvePartOne()
    input = incrementPassword(input)
    while (not isValidPassword(input)):
        input = incrementPassword(input)
    print(input)


solvePartTwo()