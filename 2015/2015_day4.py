import hashlib

input = "bgvyzdsv"

def solvePartOne():
    hexForm = ""
    i = 1
    while True:
        hexForm = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hexForm.startswith("00000"):
            print(i)
            break
        i +=1


def solvePartTwo():
    hexForm = ""
    i = 1
    while True:
        hexForm = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hexForm.startswith("000000"):
            print(i)
            break
        i +=1
solvePartTwo()
