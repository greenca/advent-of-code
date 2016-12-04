with open('day3_input.txt') as f:
    num_valid = 0
    for row in f:
        sides = [int(l) for l in row.strip().split(' ') if l != '']
        if max(sides) < sum(sides) - max(sides):
            num_valid += 1
    print num_valid

with open('day3_input.txt') as f:
    num_valid = 0
    while True:
        row1 = f.readline()
        row2 = f.readline()
        row3 = f.readline()
        if not row1 or not row2 or not row3:
            break
        sides1 = [int(l) for l in row1.strip().split(' ') if l != '']
        sides2 = [int(l) for l in row2.strip().split(' ') if l != '']
        sides3 = [int(l) for l in row3.strip().split(' ') if l != '']
        for i in range(3):
            triangle = [sides1[i], sides2[i], sides3[i]]
            if max(triangle) < sum(triangle) - max(triangle):
                num_valid += 1
    print num_valid
