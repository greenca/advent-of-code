import re

def supportsTLS(ip):
    hypernets = re.findall(r'\w*\[(\w*)\]\w*', ip)
    for hypernet in hypernets:
        if hasABBA(hypernet):
            return False
    return hasABBA(ip)

def hasABBA(seq):
    subseqs = zip(seq, seq[1:], seq[2:], seq[3:])
    for subseq in subseqs:
        if subseq[0] == subseq[3] and subseq[1] == subseq[2] and subseq[0] != subseq[1]:
            return True
    return False

def supportsSSL(ip):
    hypernets = re.findall(r'\w*\[(\w*)\]\w*', ip)
    for hypernet in hypernets:
        ip = ip.replace('['+hypernet+']', ' ')
    supernets = ip.split(' ')
    for snet in supernets:
        subseqs = zip(snet, snet[1:], snet[2:])
        for subseq in subseqs:
            if subseq[0] == subseq[2]:
                for hnet in hypernets:
                    if hnet.find(subseq[1]+subseq[0]+subseq[1]) >= 0:
                        return True
    return False


if __name__=="__main__":
    print supportsTLS("abba[mnop]qrst") == True
    print supportsTLS("abcd[bddb]xyyx") == False
    print supportsTLS("aaaa[qwer]tyui") == False
    print supportsTLS("ioxxoj[asdfgh]zxcvbn") == True
    with open("day7_input.txt") as f:
        count = 0
        for row in f:
            if supportsTLS(row.strip()):
                count += 1
        print count
    print supportsSSL("aba[bab]xyz") == True
    print supportsSSL("xyx[xyx]xyx") == False
    print supportsSSL("aaa[kek]eke") == True
    print supportsSSL("zazbz[bzb]cdb") == True
    with open("day7_input.txt") as f:
        count = 0
        for row in f:
            if supportsSSL(row.strip()):
                count += 1
        print count
