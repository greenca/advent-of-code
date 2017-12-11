def findSteps(path):
    # Cube coordinates: https://www.redblobgames.com/grids/hexagons/
    x, y, z = 0, 0, 0
    max_distance = 0
    for direction in path.split(','):
        if direction == 'n':
            y += 1
            z -= 1
        elif direction == 's':
            y -= 1
            z += 1
        elif direction == 'ne':
            x += 1
            z -= 1
        elif direction == 'sw':
            x -= 1
            z += 1
        elif direction == 'nw':
            x -= 1
            y += 1
        elif direction == 'se':
            x += 1
            y -= 1
        if cubeDistance(x,y,z) > max_distance:
            max_distance = cubeDistance(x,y,z)
    return cubeDistance(x,y,z), max_distance
            
def cubeDistance(x, y, z):
    return (abs(x) + abs(y) + abs(z))/2

print findSteps("ne,ne,ne")[0] == 3
print findSteps("ne,ne,sw,sw")[0] == 0
print findSteps("ne,ne,s,s")[0] == 2
print findSteps("se,sw,se,sw,sw")[0] == 3

with open('day11_input.txt') as f:
    input = f.read().strip()
    finalDist, maxDist = findSteps(input)
    print "Final Distance: {}".format(finalDist)
    print "Maximum Distance: {}".format(maxDist)
