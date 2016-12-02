def calculated_path(str):
    seq = str.split(', ')
    east_west = 0
    north_south = 0
    facing = 0
    for step in seq:
        direction = step[0]
        num_blocks = int(step[1:])
        if direction == 'L':
            facing -= 1
        else:
            facing += 1
        facing %= 4
        if facing % 2 == 1:
            east_west += (facing - 2)*num_blocks
        else:
            north_south += (facing - 1)*num_blocks
    return abs(east_west) + abs(north_south)

def repeated_location(str):
    seq = str.split(', ')
    east_west = 0
    north_south = 0
    facing = 0
    locations = [(0,0)]
    for step in seq:
        direction = step[0]
        num_blocks = int(step[1:])
        if direction == 'L':
            facing -= 1
        else:
            facing += 1
        facing %= 4
        for i in range(num_blocks):
            if facing % 2 == 1:
                east_west += (facing - 2)
            else:
                north_south += (facing - 1)
            if (east_west, north_south) in locations:
                return abs(east_west) + abs(north_south)
            else:
                locations.append((east_west, north_south))
    return "Not found"



if __name__=='__main__':
    print calculated_path("R2, L3")  == 5
    print calculated_path("R2, R2, R2") == 2
    print calculated_path("R5, L5, R5, R3") == 12
    print repeated_location("R8, R4, R4, R8") == 4
    with open('day1_input.txt') as f:
        input = f.read()
        print calculated_path(input)
        print repeated_location(input)

