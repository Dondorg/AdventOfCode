from AOC import *

def isNiceStringPartOne(inp):
    vowels = "aeiou"
    vowelCount = 0
    curr, prev = "-" , "-"
    hasDouble = False
    badCombos = ["ab", "cd", "pq", "xy"]
    for i in range(len(inp)):
        curr = inp[i]
        if curr in vowels:
            vowelCount += 1
        if curr == prev:
            hasDouble = True
        if prev+curr in badCombos:
            return 0
        prev = curr
    if hasDouble and (vowelCount >= 3):
        return 1
    return 0

def isNiceStringPartTwo(inp):
    curr, prev, preprev = "-","-","-"
    hasDoubleWithGap, hasRepeatPair = False, False
    for i in range(len(inp)):
        curr = inp[i]
        if preprev == curr:
            hasDoubleWithGap = True   
        if prev+curr in inp[i+1:]:
            hasRepeatPair = True     
        if hasDoubleWithGap and hasRepeatPair:
            return 1
        preprev = prev
        prev = curr
    return 0
    

def solvePartOne():
    print(sum([isNiceStringPartOne(line) for line in readInput(2015,5)]))

def solvePartTwo():
    print(sum([isNiceStringPartTwo(line) for line in readInput(2015,5)]))
