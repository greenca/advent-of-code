def Solo(filename):
    registers = {}
    lastSound = 0
    with open(filename) as f:
        instructions = f.read().split('\n')
    i = 0
    while i < len(instructions):
        instr = instructions[i].split()
        next_ind = i+1
        if instr[1].strip('-').isdigit():
            X = int(instr[1])
        else:
            X = registers.get(instr[1], 0)
        if len(instr) > 2:
            if instr[2].strip('-').isdigit():
                Y = int(instr[2])
            else:
                Y = registers.get(instr[2], 0)
        if instr[0] == 'snd':
            lastSound = X
        elif instr[0] == 'set':
            registers[instr[1]] = Y
        elif instr[0] == 'add':
            registers[instr[1]] = X + Y
        elif instr[0] == 'mul':
            registers[instr[1]] =  X * Y
        elif instr[0] == 'mod':
            registers[instr[1]] = X % Y
        elif instr[0] == 'rcv':
            if X != 0:
                return lastSound
        elif instr[0] == 'jgz':
            if X > 0:
                next_ind = i + Y
        i = next_ind
    return None

print Solo('day18_test.txt') == 4
print Solo('day18_input.txt')



queue0 = []
queue1 = []

def Duet(filename):
    registers0 = {'p': 0}
    registers1 = {'p': 1}
    sendCount = 0
    with open(filename) as f:
        instructions = f.read().split('\n')
    i0 = 0
    i1 = 0
    while True:
        registers0, next_i0, sendCount = ExecuteInstruction(0, instructions, registers0, i0, sendCount)
        registers1, next_i1, sendCount = ExecuteInstruction(1, instructions, registers1, i1, sendCount)
        if next_i0 == i0 and next_i1 == i1:
            # Deadlock
            break
        else:
            i0, i1 = next_i0, next_i1
    return sendCount


def ExecuteInstruction(pid, instructions, registers, i, sendCount):
    instr = instructions[i].split()
    next_ind = i+1
    if instr[1].strip('-').isdigit():
        X = int(instr[1])
    else:
        X = registers.get(instr[1], 0)
    if len(instr) > 2:
        if instr[2].strip('-').isdigit():
            Y = int(instr[2])
        else:
            Y = registers.get(instr[2], 0)
    if instr[0] == 'snd':
        if pid == 0:
            queue1.append(X)
        else:
            sendCount += 1
            queue0.append(X)
    elif instr[0] == 'set':
        registers[instr[1]] = Y
    elif instr[0] == 'add':
        registers[instr[1]] = X + Y
    elif instr[0] == 'mul':
        registers[instr[1]] =  X * Y
    elif instr[0] == 'mod':
        registers[instr[1]] = X % Y
    elif instr[0] == 'rcv':
        if pid == 0:
            if queue0:
                registers[instr[1]] = queue0.pop(0)
            else:
                next_ind = i
        else:
            if queue1:
                registers[instr[1]] = queue1.pop(0)
            else:
                next_ind = i
    elif instr[0] == 'jgz':
        if X > 0:
            next_ind = i + Y
    return registers, next_ind, sendCount


print Duet('day18_test2.txt') == 3
print Duet('day18_input.txt')
