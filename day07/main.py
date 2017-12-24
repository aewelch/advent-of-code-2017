from functools import reduce

class Program:
    def __init__(self, weight, balanced):
        self.weight = int(weight)
        self.balanced = balanced

    def getProgramsOnDisc(self):
        return [puzzleInput[program] for program in self.balanced]

    def getCumulativeWeight(self):
        weightOnDisk = sum([p.getCumulativeWeight() for p in self.getProgramsOnDisc()])
        return self.weight + weightOnDisk

    def isBalanced(self):
        return len(set(p.getCumulativeWeight() for p in self.getProgramsOnDisc())) == 1

def getInput():
    file = open("input.txt", "r")
    puzzleInput = file.read().strip()
    lines = puzzleInput.splitlines()

    programs = {}
    for line in lines:
        name = line.split()[0]
        weight = line.split()[1].strip('()')
        balanced = line.split(' -> ')[1].split(', ') if ' -> ' in line else []
        programs[name] = Program(weight, balanced)

    return programs

def getCorrectWeightOfUnbalancedProgram(program):
    if program.isBalanced():
        return None

    cumulativeWeightsToPrograms = {}
    for balancedProgram in program.getProgramsOnDisc():
        cumulativeWeightsToPrograms.setdefault(balancedProgram.getCumulativeWeight(), []).append(balancedProgram)

    unbalancedProgram = next(programs[0] for programs in cumulativeWeightsToPrograms.values() if len(programs) == 1)
    difference = reduce(lambda x, y: x - y, cumulativeWeightsToPrograms.keys())

    return unbalancedProgram.weight - difference

def searchTreeForUnbalancedProgram(current):
    iterator = (searchTreeForUnbalancedProgram(p) for p in current.getProgramsOnDisc() if searchTreeForUnbalancedProgram(p) != None)
    return next(iterator, getCorrectWeightOfUnbalancedProgram(current))

def partTwo(root):
    rootProgram = puzzleInput[root]
    return searchTreeForUnbalancedProgram(rootProgram)

def partOne():
    programs = set(puzzleInput.keys())
    balanced = set(b for program in puzzleInput.values() for b in program.balanced)
    return (programs - balanced).pop()

puzzleInput = getInput()
bottomProgram = partOne()

print(bottomProgram)
print(partTwo(bottomProgram))
