def isWall(x, y, fav_num):
    val = bin(x*x + 3*x + 2*x*y + y + y*y + fav_num)
    if val.count('1') % 2 == 0:
        return False
    return True

def findRoute(target_x, target_y, num):
    moves = [(1, 1, 0)]  # (x, y, steps)
    visited = [(1, 1)]
    while moves:
        x, y, steps = moves.pop(0)
        if x == target_x and y == target_y:
            return steps
        if not isWall(x+1, y, num) and (x+1, y) not in visited:
            moves.append((x+1, y, steps+1))
            visited.append((x+1, y))
        if x > 0 and not isWall(x-1, y, num) and (x-1, y) not in visited:
            moves.append((x-1, y, steps+1))
            visited.append((x-1, y))
        if not isWall(x, y+1, num) and (x, y+1) not in visited:
            moves.append((x, y+1, steps+1))
            visited.append((x, y+1))
        if y > 0 and not isWall(x, y-1, num) and (x, y-1) not in visited:
            moves.append((x, y-1, steps+1))
            visited.append((x, y-1))

def findLocations(max_steps, num):
    moves = [(1, 1, 0)]  # (x, y, steps)
    visited = [(1, 1)]
    locations = []
    while moves:
        x, y, steps = moves.pop(0)
        if steps <= max_steps:
            if (x,y) not in locations:
                locations.append((x,y))
        else:
            return len(locations)
        if not isWall(x+1, y, num) and (x+1, y) not in visited:
            moves.append((x+1, y, steps+1))
            visited.append((x+1, y))
        if x > 0 and not isWall(x-1, y, num) and (x-1, y) not in visited:
            moves.append((x-1, y, steps+1))
            visited.append((x-1, y))
        if not isWall(x, y+1, num) and (x, y+1) not in visited:
            moves.append((x, y+1, steps+1))
            visited.append((x, y+1))
        if y > 0 and not isWall(x, y-1, num) and (x, y-1) not in visited:
            moves.append((x, y-1, steps+1))
            visited.append((x, y-1))
    


if __name__=="__main__":
    walls = ['.#.####.##', '..#..#...#', '#....##...', '###.#.###.', '.##..#..#.', '..##....#.', '#...##.###']
    for y in range(7):
        row = ''
        for x in range(10):
            if isWall(x, y, 10):
                row += '#'
            else:
                row += '.'
        print row == walls[y]
    print findRoute(7, 4, 10) == 11
    print findRoute(31, 39, 1362)
    print findLocations(50, 1362)
