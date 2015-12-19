badpairs = ['ab', 'cd', 'pq', 'xy']
vowels = 'aeiou'

def checkword(word):
    word = word.lower()
    for pair in badpairs:
        if word.find(pair) >= 0:
            return False
    num_vowels = 0
    for v in vowels:
        num_vowels += word.count(v)
    doubles = False
    for i, letter in enumerate(word):
        if i>0:
            if letter == word[i-1]:
                doubles = True
    return doubles and num_vowels >= 3

assert(checkword('ugknbfddgicrmopn'))
assert(checkword('aaa'))
assert(not checkword('jchzalrnumimnmhp'))
assert(not checkword('haegwjzuvuyypxyu'))
assert(not checkword('dvszwmarrgswjxmb'))




def checkword2(word):
    word = word.lower()
    repeatedpair = False
    repeatedletter = False
    for i in range(len(word)-1):
        if word[i+2:].find(word[i:i+2]) >= 0:
            repeatedpair = True
        if i < len(word)-2:
            if word[i] == word[i+2]:
                repeatedletter = True
    return repeatedpair and repeatedletter

assert(checkword2('qjhvhtzxzqqjkmpb'))
assert(checkword2('xxyxx'))
assert(not checkword2('uurcxstgmygtbstg'))
assert(not checkword2('ieodomkazucvgmuy'))


nice_words = 0
nice_words2 = 0

with open('day5_input.txt') as f:
    for word in f:
        if checkword(word):
            nice_words += 1
        if checkword2(word):
            nice_words2 += 1


print nice_words
print nice_words2
