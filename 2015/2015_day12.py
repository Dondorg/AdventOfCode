from os import read
from AOC import *
import re
import json

def extractNumbers(text):
    return list(map(int, re.findall('-*[0-9]+', text)))

def solvePartOne():
    inp = readInput(2015,12)
    print(sum(extractNumbers(inp)))


def redDropper(thing):
    if "red" in thing.values():
        return {}
    return thing


def solvePartTwo():
    inp = readInput(2015,12)
    cleanInp = str(json.loads(inp, object_hook=redDropper))
    print(sum(extractNumbers(cleanInp)))
