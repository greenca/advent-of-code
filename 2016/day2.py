def calculateCode(instructions):
    code = ''
    cur_button = 5
    for instr in instructions:
        for move in instr:
            if move == 'U':
                if cur_button > 3:
                    cur_button -= 3
            elif move == 'D':
                if cur_button < 7:
                    cur_button += 3
            elif move == 'L':
                if cur_button % 3 != 1:
                    cur_button -= 1
            elif move == 'R':
                if cur_button % 3 != 0:
                    cur_button += 1
        code += str(cur_button)
    return code

def diamondCode(instructions):
    code = ''
    cur_button = 5
    for instr in instructions:
        for move in instr:
            if move == 'U':
                if cur_button not in [1,2,4,5,9]:
                    if cur_button in [3,13]:
                        cur_button -= 2
                    else:
                        cur_button -= 4
            elif move == 'D':
                if cur_button not in [5,9,10,12,13]:
                    if cur_button in [1,11]:
                        cur_button += 2
                    else:
                        cur_button += 4
            elif move == 'L':
                if cur_button not in [1,2,5,10,13]:
                    cur_button -= 1
            elif move == 'R':
                if cur_button not in [1,4,9,12,13]:
                    cur_button += 1
        if cur_button < 10:
            code += str(cur_button)
        else:
            code += 'ABCD'[cur_button - 10]
    return code

if __name__=='__main__':
    print calculateCode(['ULL', 'RRDDD', 'LURDL', 'UUUUD']) == '1985'
    print diamondCode(['ULL', 'RRDDD', 'LURDL', 'UUUUD']) == '5DB3'
    with open('day2_input.txt') as f:
        input = f.read().strip().split('\n')
        print calculateCode(input)
        print diamondCode(input)
