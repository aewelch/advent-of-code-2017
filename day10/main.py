import operator
import functools

def reverse(numbers, position, length):
    numbersToReverse = [numbers[(position + i) % len(numbers)] for i in range(length)]
    numbersToReverse.reverse()

    for i in range(length):
        numbers[(position + i) % len(numbers)] = numbersToReverse[i]

def runRounds(n, lengths):
    sparseHash = list(range(256))
    currentPosition = 0
    skipSize = 0

    for _ in range(n):
        for length in lengths:
            reverse(sparseHash, currentPosition, length)
            currentPosition = (currentPosition + length + skipSize) % len(sparseHash)
            skipSize += 1

    return sparseHash

def partOne():
    lengths = [int(length) for length in puzzleInput.split(',')]
    numbers = runRounds(1, lengths)
    return numbers[0] * numbers[1]

def partTwo():
    lengths = [ord(char) for char in puzzleInput]
    lengths += [17,31,73,47,23]

    sparseHash = runRounds(64, lengths)
    denseHash = [functools.reduce(lambda x, y: operator.xor(x, y), sparseHash[i:i+16]) for i in range(0, 256, 16)]

    return ''.join([format(num, '02x') for num in denseHash])

puzzleInput = "230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167"

print(partOne())
print(partTwo())
