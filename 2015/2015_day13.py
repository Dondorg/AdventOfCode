from itertools import permutations
from AOC import *

people = {}

def buildHappinessDataStruct(lines):
    modifier = 1
    for line in lines:
        line = line[:-1].split(" ")
        if line[2] == "lose":
            modifier = -1
        else:
            modifier = 1
        if not line[0] in people:
            people[line[0]] = {}
        people[line[0]][line[10]] = int(line[3])*modifier

def calcArrangementHappiness(sa):
    totalHappiness = 0
    for i in range(len(sa) - 1):
        totalHappiness += people[sa[i]][sa[i+1]]
        totalHappiness += people[sa[i+1]][sa[i]]
    totalHappiness += people[sa[0]][sa[-1]]
    totalHappiness += people[sa[-1]][sa[0]]
    return totalHappiness

def solvePartOne():
    buildHappinessDataStruct(readInput(2015,13))
    print(max(map(calcArrangementHappiness,permutations(people.keys()))))

def addYourself():
    people["me"] = {}
    for person in people:
        people[person]["me"] = 0
        people["me"][person] = 0

def solvePartTwo():
    buildHappinessDataStruct(readInput(2015,13))
    addYourself()
    print(max(map(calcArrangementHappiness,permutations(people.keys()))))

solvePartTwo()