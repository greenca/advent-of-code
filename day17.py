import itertools

containers = []
with open('day17_input.txt') as f:
    for row in f:
        containers.append(int(row.strip()))

eggnog = 150
num_comb = 0

for i in range(1, len(containers)+1):
    for group in itertools.combinations(containers, i):
        if sum(group) == eggnog:
            num_comb += 1
    if num_comb > 0:
        print i
        break

print num_comb
