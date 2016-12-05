from collections import Counter

def validID(room):
    checksum = room.split('[')[-1].strip(']')
    sectorID = int(room.split('-')[-1].split('[')[0])
    name = ''.join(room.split('-')[0:-1])
    c = Counter(name)
    letters = sorted(c.keys())
    if checksum == ''.join(sorted(letters, key = lambda l: c[l], reverse=True)[:5]):
        return sectorID
    else:
        return 0

def decryptName(room):
    sectorID = int(room.split('-')[-1].split('[')[0])
    words = room.split('-')[0:-1]
    decrypted = []
    for word in words:
        new_word = ''
        for l in word:
            new_word += chr(((ord(l) - ord('a') + sectorID) % 26) + ord('a'))
        decrypted.append(new_word)
    finalphrase = ' '.join(decrypted)
    if finalphrase.find("north") >= 0:
        print finalphrase, sectorID
    return finalphrase
        

if __name__=='__main__':
    print validID('aaaaa-bbb-z-y-x-123[abxyz]') == 123
    print validID('a-b-c-d-e-f-g-h-987[abcde]') == 987
    print validID('not-a-real-room-404[oarel]') == 404
    print validID('totally-real-room-200[decoy]') == 0
    with open('day4_input.txt') as f:
        id_sum = 0
        for row in f:
            id_sum += validID(row.strip())
            if validID(row.strip()) != 0:
                decryptName(row.strip())
        print id_sum
