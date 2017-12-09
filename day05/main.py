def getInput():
    file = open("input.txt", "r")
    puzzleInput = file.read().strip()
    return [int(s) for s in puzzleInput.splitlines()]

def stepsToExit(updateOffset):
    maze = getInput()

    steps = 0
    i = 0

    while 0 <= i < len(maze):
        jump = maze[i]
        maze[i] = updateOffset(maze[i])
        i += jump
        steps += 1

    return steps

def partOne():
    return stepsToExit(lambda n: n + 1)

def partTwo():
    return stepsToExit(lambda n: n - 1 if n >= 3 else n + 1)

print(partOne())
print(partTwo())
