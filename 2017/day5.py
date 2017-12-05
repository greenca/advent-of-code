def solveMaze(filename):
    jump_offsets = []
    with open(filename) as f:
        for row in f:
            jump_offsets.append(int(row))
    cur_index = 0
    steps = 0
    while cur_index >= 0 and cur_index < len(jump_offsets):
        new_index = cur_index + jump_offsets[cur_index]
        jump_offsets[cur_index] += 1
        cur_index = new_index
        steps += 1
    return steps

print solveMaze('day5_test.txt') == 5
print solveMaze('day5_input.txt')


def solveStrangerMaze(filename):
    jump_offsets = []
    with open(filename) as f:
        for row in f:
            jump_offsets.append(int(row))
    cur_index = 0
    steps = 0
    while cur_index >= 0 and cur_index < len(jump_offsets):
        new_index = cur_index + jump_offsets[cur_index]
        if jump_offsets[cur_index] >= 3:
            jump_offsets[cur_index] -= 1
        else:
            jump_offsets[cur_index] += 1
        cur_index = new_index
        steps += 1
    return steps

print solveStrangerMaze('day5_test.txt') == 10
print solveStrangerMaze('day5_input.txt')
