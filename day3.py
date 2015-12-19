houses = set()

pos = (0,0)
houses.add(pos)

robo_houses = set()
santa_pos = (0,0)
robo_pos = (0,0)
robo_houses.add(santa_pos)
robo_houses.add(robo_pos)
is_santa = True

with open("day3_input.txt") as f:
    instructions = f.read()
    print len(instructions)
    for c in instructions:
        if is_santa:
            cur_pos = santa_pos
        else:
            cur_pos = robo_pos
        if c == '^':
            pos = (pos[0]+1, pos[1])
            cur_pos = (cur_pos[0]+1, cur_pos[1])
        elif c == 'v':
            pos = (pos[0]-1, pos[1])
            cur_pos = (cur_pos[0]-1, cur_pos[1])
        elif c == '>':
            pos = (pos[0], pos[1]+1)
            cur_pos = (cur_pos[0], cur_pos[1]+1)
        elif c == '<':
            pos = (pos[0], pos[1]-1)
            cur_pos = (cur_pos[0], cur_pos[1]-1)
        houses.add(pos)
        robo_houses.add(cur_pos)
        if is_santa:
            santa_pos = cur_pos
            is_santa = False
        else:
            robo_pos = cur_pos
            is_santa = True

print len(houses)
print len(robo_houses)
