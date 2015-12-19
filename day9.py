import itertools

cities = ['London', 'Dublin', 'Belfast']

distances = {}
distances[('London', 'Dublin')] = 464
distances[('Dublin', 'London')] = 464
distances[('London', 'Belfast')] = 518
distances[('Belfast', 'London')] = 518
distances[('Dublin', 'Belfast')] = 141
distances[('Belfast', 'Dublin')] = 141

route_distances = []
for route in itertools.permutations(cities):
    route_dist = 0
    for i in range(len(route)-1):
        route_dist += distances[(route[i],route[i+1])]
    route_distances.append(route_dist)

assert(min(route_distances) == 605)


cities = []
distances = {}
with open('day9_input.txt') as f:
    for row in f:
        data = row.strip().split(' ')
        city1 = data[0]
        city2 = data[2]
        dist = int(data[4])
        if city1 not in cities:
            cities.append(city1)
        if city2 not in cities:
            cities.append(city2)
        distances[(city1, city2)] = dist
        distances[(city2, city1)] = dist
route_distances = []
for route in itertools.permutations(cities):
    route_dist = 0
    for i in range(len(route)-1):
        route_dist += distances[(route[i],route[i+1])]
    route_distances.append(route_dist)

print min(route_distances)
print max(route_distances)
