def init():
    global circuit, commands
    circuit = {}
    commands = {}

def update(instruction):
    instr = instruction.split(' ')
    wire = instr[-1]
    command = evaluate(instr[:-2])
    try:
        circuit[wire] = eval(command)
    except:
        commands[wire] = command

def evaluate(instr):
    if len(instr) == 1:
        return term(instr[0])
    if instr[0] == 'NOT':
        return '65536 + ~' + term(instr[1])
    if instr[1] == 'AND':
        return term(instr[0]) + ' & ' + term(instr[2])
    if instr[1] == 'OR':
        return term(instr[0]) + ' | ' + term(instr[2])
    if instr[1] == 'LSHIFT':
        return term(instr[0]) + ' << ' + term(instr[2])
    if instr[1] == 'RSHIFT':
        return term(instr[0]) + ' >> ' + term(instr[2])
    return ''

def term(x):
    if x.isdigit():
        return x
    else:
        return 'circuit["' + x + '"]'

def execute():
    remaining = commands.keys()
    while remaining:
        tmp = []
        for key in remaining:
            try:
                circuit[key] = eval(commands[key])
            except:
                tmp.append(key)
        if len(tmp) == len(remaining):
            break
        remaining = tmp


# init()
# # update('123 -> x')
# # update('456 -> y')
# update('x AND y -> d')
# update('x OR y -> e')
# update('x LSHIFT 2 -> f')
# update('y RSHIFT 2 -> g')
# update('NOT x -> h')
# update('NOT y -> i')
# update('123 -> x')
# update('456 -> y')
# execute()

instructions = [
'123 -> x',
'456 -> y',
'x AND y -> d',
'x OR y -> e',
'x LSHIFT 2 -> f',
'y RSHIFT 2 -> g',
'NOT x -> h',
'NOT y -> i']

init()
for instruction in instructions:
    update(instruction)
execute()

assert(circuit['x'] == 123)
assert(circuit['y'] == 456)
assert(circuit['d'] == 72)
assert(circuit['e'] == 507)
assert(circuit['f'] == 492)
assert(circuit['g'] == 114)
assert(circuit['h'] == 65412)
assert(circuit['i'] == 65079)


init()
with open('day7_input.txt') as f:
    for instruction in f:
        try:
            update(instruction.strip())
        except:
            print instruction
execute()

print circuit['a']

override = str(circuit['a']) + ' -> b'

init()
update(override)
with open('day7_input.txt') as f:
    for instruction in f:
        if instruction.strip().split(' ')[-1] == 'b':
            continue
        try:
            update(instruction.strip())
        except:
            print instruction
execute()

print circuit['a']
