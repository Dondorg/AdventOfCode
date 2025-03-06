from AOC import *

def parseInput():
    lines = readInput(2015, 2)
    return [list(map(lambda x: int(x), line.split("x"))) for line in lines]

def calculatePaper(dims):
    side1 = dims[0]*dims[1]
    side2 = dims[0]*dims[2]
    side3 = dims[1] *dims[2]
    area = 2*(side1 + side2 +side3) + min(side1,side2,side3)
    return area

def calculateRibbons(dims):
    perim = 2 * (sum(dims) - max(dims))
    bow = dims[0]*dims[1]*dims[2]
    return perim + bow

def solvePartOne():
    allDimensions = parseInput()
    print(sum([calculatePaper(dims) for dims in allDimensions]))

def solvePartTwo():
    allDimensions = parseInput()
    print(sum([calculateRibbons(dims) for dims in allDimensions]))
