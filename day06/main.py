def detectInfiniteLoop():
    puzzleInput = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
    redistributions = 0
    configurations = {}

    while tuple(puzzleInput) not in configurations:
        redistributions += 1
        configurations[tuple(puzzleInput)] = redistributions
        largestBankSize = max(puzzleInput)
        largestBankIndex = puzzleInput.index(largestBankSize)

        puzzleInput[largestBankIndex] = 0
        i = (largestBankIndex + 1) % len(puzzleInput)

        for _ in range(largestBankSize):
            puzzleInput[i] += 1
            i = (i + 1) % len(puzzleInput)

    return redistributions, configurations[tuple(puzzleInput)]

def partOne():
    redistributions, _ = detectInfiniteLoop()
    return redistributions

def partTwo():
    endOfLoop, startOfLoop = detectInfiniteLoop()
    return endOfLoop - startOfLoop + 1

print(partOne())
print(partTwo())
