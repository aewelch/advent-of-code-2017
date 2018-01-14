# with help from: https://www.redblobgames.com/grids/hexagons/

def getInput():
    file = open("input.txt", "r")
    return file.read().strip().split(',')

def getNextCoordinates(x, y, direction):
    return {
        'n': (x, y-1),
        'ne': (x+1, y-1),
        'se': (x+1, y),
        's': (x, y+1),
        'sw': (x-1, y+1),
        'nw': (x-1, y),
    }[direction]

def stepsToReach(x, y):
    return (abs(x) + abs(x + y) + abs(y)) // 2

def followPath():
    maxNumberOfSteps = 0
    x = y = 0

    for direction in getInput():
        x, y = getNextCoordinates(x, y, direction)
        maxNumberOfSteps = max(stepsToReach(x, y), maxNumberOfSteps)

    return stepsToReach(x, y), maxNumberOfSteps

partOne, partTwo = followPath()

print(partOne)
print(partTwo)
