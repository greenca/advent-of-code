def race(filename, time):
    distances = []
    with open(filename) as f:
        for row in f:
            data = row.split(' ')
            name = data[0]
            speed = int(data[3])
            duration = int(data[6])
            rest = int(data[13])
            remaining = time
            distance = 0
            while remaining > 0:
                if duration <= remaining:
                    distance += speed*duration
                    remaining -= duration + rest
                else:
                    distance += speed*remaining
                    remaining = 0
            distances.append(distance)
    return max(distances)

def points(filename, time):
    reindeer = {}
    with open(filename) as f:
        for row in f:
            data = row.split(' ')
            name = data[0]
            speed = int(data[3])
            duration = int(data[6])
            rest = int(data[13])
            reindeer[name] = {'speed': speed, 
                              'duration': duration, 
                              'rest': rest}
    points = {}
    positions = {}
    move_remain = {}
    rest_remain = {}
    for r in reindeer.keys():
        points[r] = 0
        positions[r] = 0
        move_remain[r] = reindeer[r]['duration']
        rest_remain[r] = reindeer[r]['rest']
    for i in range(time):
        for r in reindeer.keys():
            if move_remain[r] > 0:
                positions[r] += reindeer[r]['speed']
                move_remain[r] -= 1
            elif rest_remain[r] > 1:
                rest_remain[r] -= 1
            else:
                move_remain[r] = reindeer[r]['duration']
                rest_remain[r] = reindeer[r]['rest']
        winners = [w for w in reindeer.keys() if positions[w]==max(positions.values())]
        for r in winners:
            points[r] += 1
    return max(points.values())

print race('day14_input.txt', 2503)
print points('day14_input.txt', 2503)
