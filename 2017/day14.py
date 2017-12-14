def TieKnot(circular_list, lengths, cur_pos, skip_size):
    for length in lengths:
        sublist = []
        for i in range(length):
            sublist.append(circular_list[(cur_pos + i) % len(circular_list)])
        sublist.reverse()
        for i in range(length):
            circular_list[(cur_pos + i) % len(circular_list)] = sublist[i]
        cur_pos += length + skip_size
        skip_size += 1
    return circular_list, cur_pos, skip_size

def KnotHash(circular_list, byte_string):
    lengths = []
    for c in byte_string:
        lengths.append(ord(c))
    lengths += [17, 31, 73, 47, 23]
    cur_pos = 0
    skip_size = 0
    for n in range(64):
        circular_list, cur_pos, skip_size = TieKnot(circular_list, lengths, cur_pos, skip_size)
    dense_hash = []
    for i in range(16):
        element = 0
        for j in range(16):
            element ^= circular_list.pop(0)
        dense_hash.append(element)
    hash = ""
    for d in dense_hash:
        hash += '{:02x}'.format(d)
    return bin(int(hash,16))[2:].zfill(128)

def CountSquares(key):
    used_squares = 0
    for i in range(128):
        used_squares += KnotHash(range(256), key + '-' + str(i)).count('1')
    return used_squares

def CountRegions(key):
    squares = []
    for i in range(128):
        squares.append(list(KnotHash(range(256), key + '-' + str(i))))
    regions = 0
    for i in range(128):
        for j in range(128):
            if squares[i][j] == '1':
                regions += 1
                members = [(i,j)]
                while members:
                    x,y = members.pop(0)
                    squares[x][y] = 'x'
                    if x+1 < 128 and squares[x+1][y] == '1':
                        members.append((x+1,y))
                    if x > 0 and squares[x-1][y] == '1':
                        members.append((x-1,y))
                    if y+1 < 128 and squares[x][y+1] == '1':
                        members.append((x,y+1))
                    if y > 0 and squares[x][y-1] == '1':
                        members.append((x,y-1))
    return regions


test_key = "flqrgnkx"
input_key = "jzgqcdpd"

print CountSquares(test_key) == 8108
print CountSquares(input_key)

print CountRegions(test_key) == 1242
print CountRegions(input_key)
