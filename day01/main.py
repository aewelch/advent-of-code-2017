file = open("input.txt", "r")
puzzleInput = file.read().strip();

def getCaptcha(step):
    sum = 0

    for i in range(len(puzzleInput)):
        currentDigit = puzzleInput[i]
        nextDigit = puzzleInput[(i + step) % len(puzzleInput)]

        if currentDigit == nextDigit:
            sum += int(currentDigit)

    return sum

def partOne():
    return getCaptcha(1)

def partTwo():
    return getCaptcha(int(len(puzzleInput) / 2))

print(partOne())
print(partTwo())
