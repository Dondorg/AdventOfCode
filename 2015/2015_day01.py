from AOC import *

def solvePartOne(): 
    instructs = readInput(2015, 1)   
    floor = 0
    for i in range(len(instructs)):
        if instructs[i] == "(":
            floor += 1
        if instructs[i] == ")":
            floor -= 1
    print(floor)

def solvePartTwo():
    instructs = readInput(2015, 1)
    floor = 0
    for i in range(len(instructs)):
        if instructs[i] == "(":
            floor += 1
        if instructs[i] == ")":
            floor -= 1 
        if floor == -1:
            print(i + 1)
            break
