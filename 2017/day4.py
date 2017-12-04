def isValid(pp):
    if pp.find(' ') == -1:
        return False
    words = pp.split()
    for i, word in enumerate(words):
        if word in words[i+1:]:
            return False
    return True

print isValid('aa bb cc dd ee') == True
print isValid('aa bb cc dd aa') == False
print isValid('aa bb cc dd aaa') == True


def isStricter(pp):
    if pp.find(' ') == -1:
        return False
    words = map(sorted, pp.split())
    for i, word in enumerate(words):
        if word in words[i+1:]:
            return False
    return True

print isStricter('abcde fghij') == True
print isStricter('abcde xyz ecdab') == False
print isStricter('a ab abc abd abf abj') == True
print isStricter('iiii oiii ooii oooi oooo') == True
print isStricter('oiii ioii iioi iiio') == False


validCount = 0
strictCount = 0
with open('day4_input.txt') as f:
    for row in f:
        if isValid(row):
            validCount += 1
        if isStricter(row):
            strictCount += 1

print validCount
print strictCount
