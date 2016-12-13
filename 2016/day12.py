import string

def executeInstructions(filename, a=0, b=0, c=0, d=0):
    with open(filename) as f:
        instructions = map(string.strip, list(f))
    if not instructions:
        return None
    index = 0
    registers = {'a': a, 'b': b, 'c': c, 'd': d}
    while index < len(instructions):
        cur_instr = instructions[index].split()
        index_incr = 1
        if cur_instr[0] == 'cpy':
            if cur_instr[1].isdigit():
                registers[cur_instr[2]] = int(cur_instr[1])
            else:
                registers[cur_instr[2]] = registers[cur_instr[1]]
        elif cur_instr[0] == 'inc':
            registers[cur_instr[1]] += 1
        elif cur_instr[0] == 'dec':
            registers[cur_instr[1]] -= 1
        elif cur_instr[0] == 'jnz':
            if cur_instr[1].isdigit():
                if int(cur_instr[1]) != 0:
                    index_incr = int(cur_instr[2])
            else:
                if registers[cur_instr[1]] != 0:
                    index_incr = int(cur_instr[2])
        index += index_incr
    return registers
    


if __name__=="__main__":
    print executeInstructions("day12_test.txt")['a'] == 42
    print executeInstructions("day12_input.txt")
    print executeInstructions("day12_input.txt", c=1)
