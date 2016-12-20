def isOverlap(range1, range2):
    if range1[0] >= range2[0] and range1[0] <= range2[1]:
        return True
    if range1[1] >= range2[0] and range1[1] <= range2[1]:
        return True
    if range2[0] >= range1[0] and range2[0] <= range1[1]:
        return True
    if range2[1] >= range1[0] and range2[1] <= range1[1]:
        return True
    return False

def getReducedBlacklist(blacklist):
    combinedBL = []
    for r in blacklist:
        first, last = map(int, r.strip().split('-'))
        combinedBL.append([first, last])
    combinedBL.sort()
    reducedBL = []
    for first, last in combinedBL:
        overlap = False
        for i, curBL in enumerate(reducedBL):
            if isOverlap([first,last], curBL):
                reducedBL[i][0] = min(curBL[0], first)
                reducedBL[i][1] = max(curBL[1], last)
                overlap = True
        if not overlap:
            reducedBL.append([first, last])
    return reducedBL

def findFirstIP(max_val, blacklist):
    BL = getReducedBlacklist(blacklist)
    if not BL or BL[0][0] > 0:
        return 0
    for i, curBL in enumerate(BL):
        if i == len(BL)-1 or curBL[1] + 1 < BL[i+1][0]:
            return curBL[1]+1

def countIPs(max_val, blacklist):
    BL = getReducedBlacklist(blacklist)
    if not BL:
        return max_val+1
    numIPs = BL[0][0]
    for i, curBL in enumerate(BL):
        if i < len(BL)-1:
            numIPs += BL[i+1][0] - curBL[1] - 1
        else:
            numIPs += max_val - curBL[1]
    return numIPs
        

if __name__=="__main__":
    print findFirstIP(9, ["5-7", "0-2", "4-8"]) == 3
    with open("day20_input.txt") as f:
        blacklist = list(f)
        maxIP = 4294967295
        print findFirstIP(maxIP, blacklist)
        print countIPs(maxIP, blacklist)
