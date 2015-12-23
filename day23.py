# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).


instructions = []
with open('day23_input.txt') as f:
    for row in f:
        instructions.append(row.strip())

#registers = {'a': 0, 'b': 0}
registers = {'a': 1, 'b': 0}

i = 0
while i < len(instructions) and i >= 0:
    instr = instructions[i].split(' ')
    
    if instr[0] == 'hlf':
        registers[instr[1]] /= 2
        i += 1
    elif instr[0] == 'tpl':
        registers[instr[1]] *= 3
        i += 1
    elif instr[0] == 'inc':
        registers[instr[1]] += 1
        i += 1
    elif instr[0] == 'jmp':
        i += int(instr[1])
    elif instr[0] == 'jie':
        if registers[instr[1].strip(',')] % 2 == 0:
            i += int(instr[2])
        else:
            i += 1
    elif instr[0] == 'jio':
        if registers[instr[1].strip(',')] == 1:
            i += int(instr[2])
        else:
            i += 1

print registers
