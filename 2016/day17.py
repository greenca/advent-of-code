import md5

def findPath(passcode):
    start = (0,0)
    vault = (3,3)
    moves = [(start, '')]  # (position, path-taken)
    while moves:
        cur_pos, path = moves.pop(0)
        if cur_pos == vault:
            return path
        lock_status = md5.new(passcode+path).hexdigest()[:4]
        if cur_pos[1] > 0 and lock_status[0] in 'bcdef':
            moves.append(((cur_pos[0], cur_pos[1]-1), path+'U'))
        if cur_pos[1] < 3 and lock_status[1] in 'bcdef':
            moves.append(((cur_pos[0], cur_pos[1]+1), path+'D'))
        if cur_pos[0] > 0 and lock_status[2] in 'bcdef':
            moves.append(((cur_pos[0]-1, cur_pos[1]), path+'L'))
        if cur_pos[0] < 3 and lock_status[3] in 'bcdef':
            moves.append(((cur_pos[0]+1, cur_pos[1]), path+'R'))

def longestPath(passcode):
    start = (0,0)
    vault = (3,3)
    moves = [(start, '')]  # (position, path-taken)
    max_len = 0
    while moves:
        cur_pos, path = moves.pop(0)
        if cur_pos != vault:
            lock_status = md5.new(passcode+path).hexdigest()[:4]
            if cur_pos[1] > 0 and lock_status[0] in 'bcdef':
                moves.append(((cur_pos[0], cur_pos[1]-1), path+'U'))
            if cur_pos[1] < 3 and lock_status[1] in 'bcdef':
                moves.append(((cur_pos[0], cur_pos[1]+1), path+'D'))
            if cur_pos[0] > 0 and lock_status[2] in 'bcdef':
                moves.append(((cur_pos[0]-1, cur_pos[1]), path+'L'))
            if cur_pos[0] < 3 and lock_status[3] in 'bcdef':
                moves.append(((cur_pos[0]+1, cur_pos[1]), path+'R'))
        else:
            if len(path) > max_len:
                max_len = len(path)
    return max_len


if __name__=="__main__":
    print findPath("ihgpwlah") == "DDRRRD"
    print findPath("kglvqrro") == "DDUDRLRRUDRD"
    print findPath("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"
    print findPath("mmsxrhfx")
    print longestPath("ihgpwlah") == 370
    print longestPath("kglvqrro") == 492
    print longestPath("ulqzkmiv") == 830
    print longestPath("mmsxrhfx")
