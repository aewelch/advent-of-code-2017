def getInput():
    file = open("input.txt", "r")
    return file.read().strip()

def processStream():
    puzzleInput = getInput()

    score = 0
    depth = 0
    characterCount = 0
    isGarbage = False
    ignoreLetter = False

    for letter in puzzleInput:
        if ignoreLetter:
            ignoreLetter = False
        elif letter == '!':
            ignoreLetter = True
        elif letter == '>':
            isGarbage = False
        elif isGarbage:
            characterCount = characterCount + 1
        elif letter == '<':
            isGarbage = True
        elif letter == '{':
            depth = depth + 1
        elif letter == '}':
            score = score + depth
            depth = depth - 1

    return score, characterCount

partOne, partTwo = processStream()

print(partOne)
print(partTwo)
