import itertools

def arrange(filename):
    point_map = {}
    with open(filename) as f:
        for row in f:
            pairing = row.split(' ')
            person1 = pairing[0]
            points = int(pairing[3])
            if pairing[2] == 'lose':
                points = -points
            person2 = pairing[-1].strip('.\n')
            if person1 not in point_map.keys():
                point_map[person1] = {}
            point_map[person1][person2] = points
    all_points = []
    for ordering in itertools.permutations(point_map.keys()):
        order_points = 0
        for i in range(-1, len(ordering)-1):
            order_points += point_map[ordering[i]][ordering[i+1]] 
            order_points += point_map[ordering[i+1]][ordering[i]]
        all_points.append(order_points)
    return max(all_points)

def arrangeApathetic(filename):
    point_map = {}
    with open(filename) as f:
        for row in f:
            pairing = row.split(' ')
            person1 = pairing[0]
            points = int(pairing[3])
            if pairing[2] == 'lose':
                points = -points
            person2 = pairing[-1].strip('.\n')
            if person1 not in point_map.keys():
                point_map[person1] = {}
            point_map[person1][person2] = points
    point_map['Me'] = {}
    for person in point_map.keys():
        point_map['Me'][person] = 0
        point_map[person]['Me'] = 0
    all_points = []
    for ordering in itertools.permutations(point_map.keys()):
        order_points = 0
        for i in range(-1, len(ordering)-1):
            order_points += point_map[ordering[i]][ordering[i+1]] 
            order_points += point_map[ordering[i+1]][ordering[i]]
        all_points.append(order_points)
    return max(all_points)
    

assert(arrange('day13_test.txt')==330)
print arrange('day13_input.txt')
print arrangeApathetic('day13_input.txt')
