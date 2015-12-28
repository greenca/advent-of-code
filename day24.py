import itertools
import operator

def can_split(group):
    total = sum(group)
    for i in range(len(group)):
        for subgroup in itertools.combinations(group, i):
            if 2*sum(subgroup) == total:
                return True
    return False

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def can_div3(group):
    total = sum(group)
    for i in range(len(group)):
        for subgroup in itertools.combinations(group, i):
            if 3*sum(subgroup) == total and can_split([g for g in group if g not in subgroup]):
                return True
    return False


parcels = []
with open('day24_input.txt') as f:
    for row in f:
        parcels.append(int(row.strip()))


success = []
group1_size = 0

while not success:
    group1_size += 1
    for group1 in itertools.combinations(parcels, group1_size):
        others = [p for p in parcels if p not in group1]
        if 2*sum(group1) == sum(others):
            if can_split(others):
                success.append(group1)
            else:
                fail += 1

quantum = [prod(group) for group in success]
print min(quantum)


success = []
group1_size = 0

while not success:
    group1_size += 1
    for group1 in itertools.combinations(parcels, group1_size):
        others = [p for p in parcels if p not in group1]
        if 3*sum(group1) == sum(others):
            if can_div3(others):
                success.append(group1)
            else:
                fail += 1

quantum = [prod(group) for group in success]
print min(quantum)
