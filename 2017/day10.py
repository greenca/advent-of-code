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


result, c, s = TieKnot(range(5), [3, 4, 1, 5], 0, 0)
print result[0]*result[1] == 12
result, c, s = TieKnot(range(256), [197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63], 0, 0) 
print result[0]*result[1]


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
    return hash


print KnotHash(range(256), "") == "a2582a3a0e66e6e86e3812dcb672a272"
print KnotHash(range(256), "AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
print KnotHash(range(256), "1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
print KnotHash(range(256), "1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

print KnotHash(range(256), "197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63")
