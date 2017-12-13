def findConnections(filename):
    connections = {}
    
    with open(filename) as f:
        for row in f:
            programs = row.strip().split(' <-> ')
            connections[programs[0]] = programs[1].split(', ')

    group = ['0']
    cur_step = connections['0']
    while cur_step:
        next_step = []
        for p in cur_step:
            if p not in group:
                group.append(p)
                next_step += connections[p]
        cur_step = next_step

    return len(group)

print findConnections('day12_test.txt') == 6
print findConnections('day12_input.txt')


def findGroups(filename):
    connections = {}

    with open(filename) as f:
        for row in f:
            programs = row.strip().split(' <-> ')
            connections[programs[0]] = programs[1].split(', ')

    groups = []
    connected_programs = []
    for program in connections:
        if program not in connected_programs:
            cur_group = [program]
            cur_step = connections[program]
            while cur_step:
                next_step = []
                for p in cur_step:
                    if p not in cur_group:
                        connected_programs.append(p)
                        cur_group.append(p)
                        next_step += connections[p]
                cur_step = next_step
            groups.append(cur_group)

    return len(groups)

print findGroups('day12_test.txt') == 2
print findGroups('day12_input.txt')
