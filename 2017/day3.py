import math

def findSquare(square):
    cur_ring_start = 1
    next_ring_start = 2
    side_len = 1
    
    while next_ring_start <= square:
        next_side_len = side_len + 2
        cur_ring_start = next_ring_start
        next_ring_start = cur_ring_start + 4*next_side_len - 4
        side_len = next_side_len
        
    if cur_ring_start == 1:
        corners = [1,1,1,1]
    else:
        corners = [cur_ring_start + side_len - 2, cur_ring_start + 2*side_len - 3, cur_ring_start + 3*side_len - 4, cur_ring_start + 4*side_len - 5]

    corner_position = (side_len - 1)/2
    
    for c in corners:
        if square <= c:
            square_position = corner_position - (c - square)
            break

    return abs(square_position) + corner_position


def allocateSquares(min_value):
    values = {(0,0): 1, (1,0): 1}

    row, col = 1, 0
    ring_start = 2
    side_len = 3
    cur_val = 1

    while cur_val <= min_value:
        corner_position = (side_len - 1)/2
        if row == corner_position:
            if col == -corner_position:
                ring_start = ring_start + 4*side_len - 4
                side_len += 2
                row += 1
            elif col < corner_position:
                col += 1
            else:
                row -= 1
        elif col == corner_position:
            if row > -corner_position:
                row -= 1
            else:
                col -= 1
        elif row == -corner_position:
            if col > -corner_position:
                col -= 1
            else:
                row += 1
        else:
            row += 1
                
        cur_val = 0
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                cur_val += values.get((r,c), 0)

        values[(row, col)] = cur_val

    return cur_val


print findSquare(1) == 0
print findSquare(12) == 3
print findSquare(23) == 2
print findSquare(1024) == 31
print findSquare(289326)


print allocateSquares(289326)
