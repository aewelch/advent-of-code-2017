import itertools

def splitRows(rows):
    return [[int(s) for s in row.split("\t")] for row in rows]

def getInputRows():
    file = open("input.txt", "r")
    puzzleInput = file.read()
    rows = puzzleInput.splitlines()
    return splitRows(rows)

def getDifference(values):
    smallestValue = values[0]
    largestValue = values[0]

    for value in values:
        smallestValue = min(smallestValue, value)
        largestValue = max(largestValue, value)

    return largestValue - smallestValue

def getDivision(values):
    for a, b in itertools.combinations(values, 2):
        maxValue = max(a, b)
        minValue = min(a, b)

        if maxValue % minValue == 0:
            return maxValue / minValue

def partOne():
    checksum = 0

    for row in getInputRows():
        checksum += getDifference(row)

    return checksum

def partTwo():
    checksum = 0

    for row in getInputRows():
        checksum += getDivision(row)

    return checksum

print(partOne())
print(partTwo())
