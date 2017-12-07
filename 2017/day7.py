parents = {}
children = {}
all_children = []

#with open('day7_test.txt') as f:
with open('day7_input.txt') as f:
    for row in f:
        items = row.split()
        parents[items[0]] = int(items[1].strip('()'))
        children[items[0]] = []
        for child in items[3:]:
            children[items[0]].append(child.strip(','))
            all_children.append(child.strip(','))

for p in parents:
    if p not in all_children:
        print p

def getStackWeight(c):
    weight = parents[c]
    for child in children[c]:
        weight += getStackWeight(child)
    return weight


unbalanced = []
for p in parents:
    if children[p]:
        child_weights = []
        for c in children[p]:
            child_weights.append(getStackWeight(c))
        if max(child_weights) != min(child_weights):
            unbalanced.append(p)


wrong_weight = [p for p in unbalanced]
for p in unbalanced:
    for c in children[p]:
        if c in unbalanced:
            wrong_weight.remove(p)

weights = [getStackWeight(c) for c in children[wrong_weight[0]]]
if weights.count(max(weights)) == 1:
    print parents[children[wrong_weight[0]][weights.index(max(weights))]] - (max(weights)-min(weights))
else:
    print parents[children[wrong_weight[0]][weights.index(min(weights))]] + (max(weights)-min(weights))
