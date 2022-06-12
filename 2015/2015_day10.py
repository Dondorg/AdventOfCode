from AOC import *

def nextLookAndSay(sequence):
    currentDigit = ""
    currentDigitCount = 0
    newSequence=""
    for i in range(len(sequence)):
        if currentDigit == sequence[i]:
            currentDigitCount += 1
        else:
            if currentDigitCount > 0:
                newSequence += str(currentDigitCount) + currentDigit          
            currentDigitCount = 1
            currentDigit = sequence[i]
    newSequence += str(currentDigitCount) + currentDigit
    return newSequence

def solvePartOne():
    input = readInput(2015, 10)
    for i in range(40):
        input = nextLookAndSay(input)

    print(len(input))

def solvePartTwo():
    input = readInput(2015, 10)
    for i in range(50):
        input = nextLookAndSay(input)

    print(len(input))

solvePartOne()