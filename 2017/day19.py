def FollowRoute(filename):
    with open(filename) as f:
        route = f.read().split('\n')
    route = [r for r in route if r!=""]
    direction = 'D'
    row,col = 0, route[0].index('|')
    cur_val = route[row][col]
    output = ''
    steps = 0
    while cur_val != " ":
        steps += 1
        if direction == 'D':
            row += 1
        elif direction == 'U':
            row -= 1
        elif direction == 'R':
            col += 1
        elif direction == 'L':
            col -= 1
        if row >=0 and row < len(route) and col >= 0 and col < len(route[row]):
            cur_val = route[row][col]
        else:
            cur_val = " "
        if cur_val.isalpha():
            output += cur_val
        elif cur_val == '+':
            if direction == 'D' or direction == 'U':
                if col == 0:
                    direction = 'R'
                elif col == len(route[row])-1:
                    direction = 'L'
                elif route[row][col-1] == '-' or (route[row][col-1].isalpha() and route[row][col+1] != '-'):
                    direction = 'L'
                else:
                    direction = 'R'
            elif direction == 'L' or direction == 'R':
                if row == 0:
                    direction = 'D'
                elif row == len(route)-1:
                    direction = 'U'
                elif route[row+1][col] == '|' or (route[row+1][col].isalpha() and route[row-1][col] != '|'):
                    direction = 'D'
                else:
                    direction = 'U'
    return output, steps
                    


print FollowRoute('day19_test.txt') == ("ABCDEF", 38)
print FollowRoute('day19_input.txt')
