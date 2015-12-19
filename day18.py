num_steps = 100
init_config = []

with open('day18_input.txt') as f:
    for row in f:
        init_config.append(list(row.strip()))

num_rows = len(init_config)
num_cols = len(init_config[0])

cur_config = init_config
cur_config[0][0] = '#'
cur_config[0][num_cols-1] = '#'
cur_config[num_rows-1][0] = '#'
cur_config[num_rows-1][num_cols-1] = '#'

for n in range(num_steps):
    new_config = [[cur_config[i][j] for j in range(num_cols)] for i in range(num_rows)]
    for i, row in enumerate(cur_config):
        for j, light in enumerate(row):
            neighbours = [cur_config[x][y] for x in range(max(0,i-1),min(num_rows,i+2)) for y in range(max(0,j-1),min(num_cols,j+2)) if (x,y) != (i,j)]
            neighbours_on = neighbours.count('#')
            if light == '#':
                if neighbours_on != 2 and neighbours_on != 3:
                    new_config[i][j] = '.'
            else:
                if neighbours_on == 3:
                    new_config[i][j] = '#'
    cur_config = new_config
    cur_config[0][0] = '#'
    cur_config[0][num_cols-1] = '#'
    cur_config[num_rows-1][0] = '#'
    cur_config[num_rows-1][num_cols-1] = '#'

lights_on = 0
for row in cur_config:
    lights_on += row.count('#')

print lights_on
