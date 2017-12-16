def Dance(programs, moves):
    for move in moves:
        if move[0] == 's':
            n = int(move[1:])
            programs = programs[-n:] + programs[:-n]
        elif move[0] == 'x':
            i, j = map(int, move[1:].split('/'))
            programs[i], programs[j] = programs[j], programs[i]
        elif move[0] == 'p':
            p1, p2 = move[1:].split('/')
            i = programs.index(p1)
            j = programs.index(p2)
            programs[i], programs[j] = programs[j], programs[i]
            
    return programs

def RepeatDance(programs, moves):
    permutations = []
    for i in xrange(1000000000):
        p = ''.join(programs)
        if p in permutations:
            return permutations[1000000000 % i]
        permutations.append(p)
        programs = Dance(programs, moves)
    return ''.join(programs)

programs = list("abcde")
moves = ['s1','x3/4','pe/b']
print ''.join(Dance(programs[:], moves)) == "baedc"

programs = list("abcdefghijklmnop")
with open("day16_input.txt") as f:
    moves = f.read().split(',')
print ''.join(Dance(programs[:], moves))
print RepeatDance(programs[:], moves)
