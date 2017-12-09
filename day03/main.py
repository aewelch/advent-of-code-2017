puzzleInput = 368078

def getNextCoordinates(x, y, direction):
    return {
      'N': (x-1, y),
      'E': (x, y+1),
      'S': (x+1, y),
      'W': (x, y-1)
    }[direction]

def amountToMove(sideLength, direction):
    return {
      'N': sideLength - 2,
      'E': sideLength,
      'S': sideLength - 1,
      'W': sideLength - 1
    }[direction]

def adjacentSquares(spiral, x, y):
    return [spiral.get((x+i, y+j), 0) for i in [-1, 0, 1] for j in [-1, 0, 1]]

def partOne():
    spiral = { }
    sideLength = 1
    x = y = 0
    counter = 1

    while True:
        for direction in ['N', 'W', 'S', 'E']:
            for _ in range(amountToMove(sideLength, direction)):
                spiral[(x, y)] = counter

                if spiral[(x, y)] == puzzleInput:
                    return abs(x) + abs(y)

                counter += 1
                x, y = getNextCoordinates(x, y, direction)
        sideLength +=2

    return spiral

def partTwo():
    spiral = { (0, 0): 1 }
    sideLength = 1
    x = y = 0

    while True:
        for direction in ['N', 'W', 'S', 'E']:
            for _ in range(amountToMove(sideLength, direction)):
                spiral[(x, y)] = sum(adjacentSquares(spiral, x, y))

                if spiral[(x, y)] > puzzleInput:
                    return spiral[(x, y)]

                x, y = getNextCoordinates(x, y, direction)
        sideLength +=2

    return spiral

print(partOne())
print(partTwo())
