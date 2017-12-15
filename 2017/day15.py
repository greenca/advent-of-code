factorA = 16807
factorB = 48271
denominator = 2147483647


def CompareGenerators(initA, initB):
    prevA, prevB = initA, initB
    matches = 0
    for i in xrange(40000000):
        prevA = (prevA * factorA) % denominator
        prevB = (prevB * factorB) % denominator
        if bin(prevA)[-16:] == bin(prevB)[-16:]:
            matches += 1
    return matches

print CompareGenerators(65, 8921) == 588
print CompareGenerators(516, 190)


def ComparePickyGenerators(initA, initB):
    prevA, prevB = initA, initB
    matches = 0
    for i in xrange(5000000):
        prevA = (prevA * factorA) % denominator
        while prevA % 4 != 0:
            prevA = (prevA * factorA) % denominator
        prevB = (prevB * factorB) % denominator
        while prevB % 8 != 0:
            prevB = (prevB * factorB) % denominator
        if bin(prevA)[-16:] == bin(prevB)[-16:]:
            matches += 1
    return matches

print ComparePickyGenerators(65, 8921) == 309
print ComparePickyGenerators(516, 190)
