import md5
import collections

def generateKeys(num, salt, stretch=1):
    keys = []
    hashes = collections.deque()
    for i in range(1001):
        max_index = i
        hashes.append(getHash(salt+str(i), stretch))
    cur_index = 0
    while len(keys) < num:
        cur_hash = hashes.popleft()
        c = findThree(cur_hash)
        if c and hasFive(c, hashes):
            keys.append((cur_index, cur_hash))
        max_index += 1
        hashes.append(getHash(salt+str(max_index), stretch))
        cur_index += 1
    return keys

def getHash(s, stretch):
    output = s
    for i in range(stretch):
        output = md5.new(output).hexdigest()
    return output

def findThree(s):
    for x,y,z in zip(s, s[1:], s[2:]):
        if x == y and x == z:
            return x

def hasFive(c, strings):
    for s in strings:
        for i in range(len(s)-4):
            if s[i:i+5] == 5*c:
                return True
    return False


if __name__=="__main__":
    testKeys = generateKeys(64, "abc")
    print testKeys[0][0] == 39
    print testKeys[1][0] == 92
    print testKeys[63][0] == 22728
    keys = generateKeys(64, "zpqevtbw")
    print keys[63][0]
    testStretched = generateKeys(64, "abc", 2017)
    print testStretched[0][0] == 10
    print testStretched[63][0] == 22551
    stretchedKeys = generateKeys(64, "zpqevtbw", 2017)
    print stretchedKeys[63][0]
