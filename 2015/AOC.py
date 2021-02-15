def readInput(year, day):
    filePath = "./" +str(year) + "/inputs/input" + str(day) + ".txt"
    with open(filePath) as f:
        lines = [line.strip() for line in f.readlines()]
    if len(lines) == 1:
        lines = lines[0]
    return lines