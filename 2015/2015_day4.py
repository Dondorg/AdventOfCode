import hashlib

input = "bgvyzdsv"

def solve(prefix):
    hexForm = ""
    i = 1
    while True:
        hexForm = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hexForm.startswith(prefix):
            print(i)
            break
        i +=1

def solvePartOne():
    solve("00000")

def solvePartTwo():
    solve("000000")

