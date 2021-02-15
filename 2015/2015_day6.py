import numpy as np
from AOC import *

def toggle(grid, startX, stopX, startY, stopY):
    grid[startX:stopX, startY:stopY] = (grid[startX:stopX, startY:stopY] + 1) % 2

def turnOn(grid, startX, stopX, startY, stopY):
    grid[startX:stopX, startY:stopY] = 1

def turnOff(grid, startX, stopX, startY, stopY):
    grid[startX:stopX, startY:stopY] = 0

def addTwo(grid, startX, stopX, startY, stopY):
    grid[startX:stopX, startY:stopY] += 2

def addOne(grid, startX, stopX, startY, stopY):
    grid[startX:stopX, startY:stopY] += 1

def lowerOne(grid, startX, stopX, startY, stopY):
    grid[startX:stopX, startY:stopY] =np.clip((grid[startX:stopX, startY:stopY] - 1), 0, None)

instructions1 = {"toggle": toggle, "on": turnOn, "off": turnOff}

instructions2 = {"toggle": addTwo, "on": addOne, "off": lowerOne}

instructions = [instructions1, instructions2]

def parseLine(line, problemPart):
    words = line.split(" ")
    if words[0] =="turn":
        words = words[1:]
    action = instructions[problemPart][words[0]]
    startX , startY = [int(number) for number in words[1].split(",")]
    stopX , stopY = [int(number) for number in words[3].split(",")]
    return (action, startX, stopX+1, startY, stopY+1)

def solve(problemPart):
    grid = np.zeros((1000,1000))
    for line in readInput(2015, 6):
        action, startX, startY, stopX, stopY = parseLine(line, problemPart)
        action(grid, startX, startY, stopX, stopY)
    print(grid.sum())

def solvePartOne():
    solve(0)

def solvePartTwo():
    solve(1)