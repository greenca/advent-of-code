from string import maketrans
from itertools import permutations

def swapPositions(s, x, y):
    lst = list(s)
    lst[x], lst[y] = lst[y], lst[x]
    return ''.join(lst)

def swapLetters(s, x, y):
    transtab = maketrans(x+y, y+x)
    return s.translate(transtab)

def rotateSteps(s, n):
    if n < 0:
        n = n % len(s) - len(s)
    else:
        n = n % len(s)
    return s[n:] + s[:n]

def rotateByLetter(s, letter):
    pos = s.index(letter)
    if pos < 4:
        return rotateSteps(s, -(pos+1))
    else:
        return rotateSteps(s, -(pos+2))

def reversePositions(s, x, y):
    substr = list(s[x:y+1])
    substr.reverse()
    return s[:x] + ''.join(substr) + s[y+1:]

def movePositions(s, x, y):
    if x < y:
        return s[:x] + s[x+1:y+1] + s[x] + s[y+1:]
    else:
        return s[:y] + s[x] + s[y:x] + s[x+1:]

def parseOperation(s, op):
    components = op.split()
    if components[0] == "swap":
        if components[1] == "position":
            return swapPositions(s, int(components[2]), int(components[5]))
        elif components[1] == "letter":
            return swapLetters(s, components[2], components[5])
    elif components[0] == "rotate":
        if components[1] == "based":
            return rotateByLetter(s, components[6])
        elif components[1] == "left":
            return rotateSteps(s, int(components[2]))
        elif components[1] == "right":
            return rotateSteps(s, -int(components[2]))
    elif components[0] == "reverse":
        return reversePositions(s, int(components[2]), int(components[4]))
    elif components[0] == "move":
        return movePositions(s, int(components[2]), int(components[5]))
    return s

def scramble(s, op_file):
    with open(op_file) as f:
        for op in f:
            s = parseOperation(s, op.strip())
    return s

def unscramble(s, op_file):
    for p in permutations(s):
        test_string = ''.join(p)
        if scramble(test_string, op_file) == s:
            return test_string


if __name__=="__main__":
    print parseOperation("abcde", "swap position 4 with position 0") == "ebcda"
    print parseOperation("ebcda", "swap letter d with letter b") == "edcba"
    print parseOperation("edcba", "reverse positions 0 through 4") == "abcde"
    print parseOperation("abcde", "rotate left 1 step") == "bcdea"
    print parseOperation("bcdea", "move position 1 to position 4") == "bdeac"
    print parseOperation("bdeac", "move position 3 to position 0") == "abdec"
    print parseOperation("abdec", "rotate based on position of letter b") == "ecabd"
    print parseOperation("ecabd", "rotate based on position of letter d") == "decab"
    print scramble("abcde", "day21_test.txt") == "decab"
    print scramble("abcdefgh", "day21_input.txt")
    print unscramble("fbgdceah", "day21_input.txt")
