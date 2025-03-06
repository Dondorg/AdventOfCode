from itertools import permutations
from AOC import *
import numpy as np

locations = {}
distances = np.array([])

def parseLine(line):
    tokens = line.split(" ")
    locationA, locationB = tokens[0], tokens[2]
    distance = int(tokens[-1])
    distances[locations[locationA]][locations[locationB]] = distance
    distances[locations[locationB]][locations[locationA]] = distance

def locationParse(line):
    tokens = line.split(" ")
    locationA, locationB = tokens[0], tokens[2]
    if locationA not in locations:
        locations[locationA] = len(locations)
    if locationB not in locations:
        locations[locationB] = len(locations)

def initLocations():
    for line in readInput(2015, 9):
        locationParse(line)

def initDistances():
    distances.resize((len(locations), len(locations)))
    for line in readInput(2015, 9):
        parseLine(line)

def sumRoute(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += distances[locations[route[i]]][locations[route[i+1]]]
    return distance

def bruteForceSolution(func):
    return func(map(sumRoute,permutations(locations)))

def solvePartOne():
    initLocations()
    initDistances()
    print(bruteForceSolution(min))
    print(bruteForceSolution(max))

solvePartOne()

