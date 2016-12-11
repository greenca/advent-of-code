import re

def decompress(sequence):
    seq = re.sub(r'\s+','',sequence)
    result = ''
    match = re.search(r'(\w*)\((\w*)\)(\S*)', seq)
    if not match:
        result = seq
    else:
        length = int(match.group(2).split('x')[0])
        rep = int(match.group(2).split('x')[1])
        result += match.group(1)
        for i in range(rep):
            result += match.group(3)[:length]
        result += decompress(match.group(3)[length:])
    return result

def decompress2(sequence):
    seq = re.sub(r'\s+','',sequence)
    resultLen = 0
    match = re.search(r'(\w*)\((\w*)\)(\S*)', seq)
    if not match:
        resultLen = len(seq)
    else:
        length = int(match.group(2).split('x')[0])
        rep = int(match.group(2).split('x')[1])
        resultLen += len(match.group(1))
        resultLen += rep*decompress2(match.group(3)[:length])
        resultLen += decompress2(match.group(3)[length:])
    return resultLen
    

if __name__=="__main__":
    print decompress("ADVENT") == "ADVENT"
    print decompress("A(1x5)BC") == "ABBBBBC"
    print decompress("(3x3)XYZ") == "XYZXYZXYZ"
    print decompress("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"
    print decompress("(6x1)(1x3)A") == "(1x3)A"
    print decompress("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"
    print decompress2("(3x3)XYZ") == 9
    print decompress2("X(8x2)(3x3)ABCY") == 20
    print decompress2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920
    print decompress2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445
    with open("day9_input.txt") as f:
        sequence = f.read()
        print len(decompress(sequence))
        print decompress2(sequence)
