def increment(pw):
    if not pw:
        return ''
    letters = list(pw)
    if letters[-1] == 'z':
        return increment(''.join(letters[:-1])) + 'a'
    letters[-1] = chr(ord(letters[-1])+1)
    return ''.join(letters)

def condition1(pw):
    for i in range(len(pw)-2):
        cur = ord(pw[i])
        if ord(pw[i+1]) == cur+1 and ord(pw[i+2]) == cur+2:
            return True
    return False

def condition2(pw):
    if 'i' in pw or 'l' in pw or 'o' in pw:
        return False
    return True

def condition3(pw):
    num_pairs = 0
    i = 0
    while i < len(pw)-1:
        if pw[i]==pw[i+1]:
            num_pairs += 1
            i += 2
        else:
            i += 1
    return num_pairs >= 2

assert(condition1('hijklmmn'))
assert(not condition1('abbceffg'))
assert(not condition2('hijklmmn'))
assert(condition3('abbceffg'))
assert(not condition3('abbcegjk'))

def validPassword(pw):
    return condition1(pw) and condition2(pw) and condition3(pw)

def nextPassword(pw):
    valid = False
    while not valid:
        pw = increment(pw)
        valid = validPassword(pw)
    return pw

assert(nextPassword('abcdefgh') == 'abcdffaa')
assert(nextPassword('ghijklmn') == 'ghjaabcc')

newpw = nextPassword('hepxcrrq')
print newpw

newpw2 = nextPassword(newpw)
print newpw2
