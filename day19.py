from random import shuffle

mappings = []

with open('day19_input.txt') as f:
    for row in f:
        data = row.strip().split(' => ')
        if len(data) == 2:
            mappings.append(data)
        elif data[0]:
            start = data[0]
        

molecules = set()

for orig, replace in mappings:
    prev = 0
    while orig in start[prev:]:
        molecules.add(start[:prev] + start[prev:].replace(orig,replace,1))
        prev = start.find(orig, prev+1)
        if prev == -1:
            prev = len(start)

print len(molecules)


random_steps = []
for random_trial in range(10):

    target = start
    step = 0

    while target != 'e':
        shuffle(mappings)
        tmp = target
        for orig, replace in mappings:
            if replace not in target:
                continue
            target = target.replace(replace, orig, 1)
            step += 1
        if tmp == target:
            target = start
            step = 0
    
    random_steps.append(step)

print random_steps
