from AOC import *

moves = {">": [1,0], "<": [-1,0] , "v": [0,-1], "^":[0,1]}

def solvePartOne():
    input = readInput(2015, 3)
    x, y = 0,0
    pointSet = set([(x,y)])
    for i in range(len(input)):
        x += moves[input[i]][0]
        y += moves[input[i]][1]
        pointSet.add((x,y))
    print(len(pointSet))


def solvepartTwo():
    input = readInput(2015, 3)
    x1, y1, x2,y2 = 0,0,0,0
    pointSet = set([(0,0)])
    for i in range(len(input)):
        if i%2 == 0:
            x1 += moves[input[i]][0]
            y1 += moves[input[i]][1]
            pointSet.add((x1,y1))
        else:
            x2 += moves[input[i]][0]
            y2 += moves[input[i]][1]
            pointSet.add((x2,y2))
    print(len(pointSet))
