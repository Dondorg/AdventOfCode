from AOC import *

def initReindeer(lines):
    reindeer = {}
    for line in lines:
        line = line.split(" ")
        reindeer[line[0]] = {
            "speed": int(line[3]),
            "endurance": int(line[6]), 
            "restTime": int(line[-2])
        }
    return reindeer

def distanceTraveled(totalTime,r):
    return calcdistanceTraveled(totalTime, r["endurance"], r["restTime"], r["speed"])

def calcdistanceTraveled(totalTime, travelTime, restTime, speed):
    numRuns = totalTime // (travelTime + restTime)
    remainingTime = totalTime % (travelTime + restTime)
    partialRun = min(remainingTime / travelTime, 1)
    distanceRun = (numRuns + partialRun) * travelTime * speed
    return distanceRun

def solvePartOne():
    input = readInput(2015,14)
    reindeer = initReindeer(input)
    winner = max([distanceTraveled(2503, reindeer[r])  for r in reindeer])
    print(winner)


def solvePartTwo():
    input = readInput(2015,14)
    reindeer = initReindeer(input)
    points = {r:0 for r in reindeer}
    leader = ("", 0)
    for i in range(2503):
        for r in reindeer:
            distance = distanceTraveled(i, reindeer[r])
            if distance > leader[1]:
                leader = (r, distance)
        if leader[0] in points: points[leader[0]] += 1
    print(max([points[r] for r in points]))
