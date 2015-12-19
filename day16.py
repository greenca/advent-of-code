data = {'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1}

with open('day16_input.txt') as f:
    for row in f:
        sue = row.split(' ')
        sue = [s.strip(':,\n') for s in sue]
        num = sue[1]
        match = True
        for i in range(2,len(sue)-1,2):
            if data[sue[i]] != int(sue[i+1]):
                match = False
        if match:
            print 'Exact:', sue
        range_match = True
        for i in range(2, len(sue)-1, 2):
            data_type = sue[i]
            if data_type == 'cats' or data_type == 'trees':
                if data[data_type] >= int(sue[i+1]):
                    range_match = False
            elif data_type == 'pomerians' or data_type == 'goldfish':
                if data[data_type] <= int(sue[i+1]):
                    range_match = False
            else:
                if data[data_type] != int(sue[i+1]):
                    range_match = False
        if range_match:
            print 'Range:', sue

