def split(passphrases):
    return [[word for word in passphrase.split(" ")] for passphrase in passphrases]

def getInput():
    file = open("input.txt", "r")
    puzzleInput = file.read()
    passphrases = puzzleInput.splitlines()
    return split(passphrases)

def sort(word):
    return ''.join(sorted(word))

def containsNoAnagrams(passphrase):
    return len(set([sort(word) for word in passphrase])) == len(passphrase)

def containsNoDuplicates(passphrase):
    return len(set(passphrase)) == len(passphrase)

def partOne():
    validRows = [containsNoDuplicates(passphrase) for passphrase in getInput()]
    return sum(validRows)

def partTwo():
    validRows = [containsNoAnagrams(passphrase) for passphrase in getInput()]
    return sum(validRows)

print(partOne())
print(partTwo())
