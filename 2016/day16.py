import re

def generateData(data_len, initial):
    data = initial
    while len(data) < data_len:
        new_data = list(data)
        new_data.reverse()
        data += '0'
        for c in new_data:
            if c == '0':
                data += '1'
            elif c == '1':
                data += '0'
    return data[:data_len]

def getChecksum(data):
    pairs = re.findall(r'[0|1][0|1]', data)
    checksum = ''.join([str(int(a==b)) for a,b in pairs])
    if len(checksum) % 2 == 1:
        return checksum
    else:
        return getChecksum(checksum)


if __name__=="__main__":
    print generateData(3, '1') == '100'
    print generateData(3, '0') == '001'
    print generateData(11, '11111') == '11111000000'
    print generateData(25, '111100001010') == '1111000010100101011110000'
    print getChecksum('110010110100') == '100'
    print generateData(20, '10000') == '10000011110010000111'
    print getChecksum(generateData(20, '10000')) == '01100'
    print getChecksum(generateData(272, '10010000000110000'))
    print getChecksum(generateData(35651584, '10010000000110000'))
