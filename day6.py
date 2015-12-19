lights = [[0 for i in range(1000)] for j in range(1000)]

with open('day6_input.txt') as f:
    for instruction in f:
        instr = instruction.split(' ')
        if instr[0] == 'turn':
            start = [int(i) for i in instr[2].split(',')]
            stop = [int(i) for i in instr[4].split(',')]
            change_type = instr[1]
        elif instr[0] == 'toggle':
            start = [int(i) for i in instr[1].split(',')]
            stop = [int(i) for i in instr[3].split(',')]
            change_type = 'toggle'
        for i in range(start[0], stop[0]+1):
            for j in range(start[1], stop[1]+1):
                if change_type == 'on':
                    # lights[i][j] = 1
                    lights[i][j] += 1
                elif change_type  == 'off':
                    # lights[i][j] = 0
                    lights[i][j] = max(0, lights[i][j]-1)
                elif change_type == 'toggle':
                    # lights[i][j] = int(not lights[i][j])
                    lights[i][j] += 2
            

print sum(sum(row) for row in lights)
