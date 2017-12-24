def getInput():
    file = open("input.txt", "r")
    puzzleInput = file.read().strip()
    return puzzleInput.splitlines()

operations = {
  '>': lambda x, y: x > y,
  '<': lambda x, y: x < y,
  '>=': lambda x, y: x >= y,
  '<=': lambda x, y: x <= y,
  '==': lambda x, y: x == y,
  '!=': lambda x, y: x != y,
  'inc': lambda x, y: x + y,
  'dec': lambda x, y: x - y
}

def processInstructions():
    instructions = getInput()
    registers = {}
    maxValue = 0

    for instruction in instructions:
        parts = instruction.split(' ')

        register = parts[0]
        operation = operations[parts[1]]
        amount = int(parts[2])

        conditionalRegister = parts[4]
        conditionalOperation = operations[parts[5]]
        conditionalAmount = int(parts[6])

        if register not in registers:
            registers[register] = 0

        if conditionalRegister not in registers:
            registers[conditionalRegister] = 0

        if conditionalOperation(registers[conditionalRegister], conditionalAmount):
            registers[register] = operation(registers[register], amount)

        if registers[register] > maxValue:
            maxValue = registers[register]

    return max(registers.values()), maxValue

partOne, partTwo = processInstructions()

print(partOne)
print(partTwo)
