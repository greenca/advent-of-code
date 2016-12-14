def isValid(config):
    for chip, gen in config:
        if chip < 1 or chip > 4 or gen < 1 or gen > 4:
            return False
        if chip != gen:
            if chip in [gen for chip, gen in config]:
                return False
    return True

def findRoute(initConfig):
    num_chips = len(initConfig)
    moves = [(initConfig, 1, 0)]  # (config, elevator, steps)
    visited = [(initConfig, 1)]
    while moves:
        cur_config, elevator, steps = moves.pop(0)
        fourth_floor = True
        for pair in cur_config:
            if pair != [4,4]:
                fourth_floor = False
        if fourth_floor and elevator == 4:
            return steps
        chips = [i for i in range(num_chips) if cur_config[i][0] == elevator]
        gens = [i for i in range(num_chips) if cur_config[i][1] == elevator]
        for i, chip1 in enumerate(chips):
            # move chip up
            new_config = [[chip, gen] for chip, gen in cur_config]
            new_config[chip1][0] += 1
            new_config.sort()
            if isValid(new_config) and (new_config, elevator+1) not in visited:
                moves.append((new_config, elevator+1, steps+1))
                visited.append((new_config, elevator+1))
            # move chip down
            new_config = [[chip, gen] for chip, gen in cur_config]
            new_config[chip1][0] -= 1
            new_config.sort()
            if isValid(new_config) and (new_config, elevator-1) not in visited:
                moves.append((new_config, elevator-1, steps+1))
                visited.append((new_config, elevator-1))
            for chip2 in chips[i+1:]:
                # move pair up
                new_config = [[chip, gen] for chip, gen in cur_config]
                new_config[chip1][0] += 1
                new_config[chip2][0] += 1
                new_config.sort()
                if isValid(new_config) and (new_config, elevator+1) not in visited:
                    moves.append((new_config, elevator+1, steps+1))
                    visited.append((new_config, elevator+1))
                # move pair down
                new_config = [[chip, gen] for chip, gen in cur_config]
                new_config[chip1][0] -= 1
                new_config[chip2][0] -= 1
                new_config.sort()
                if isValid(new_config) and (new_config, elevator-1) not in visited:
                    moves.append((new_config, elevator-1, steps+1))
                    visited.append((new_config, elevator-1))
            if chip1 in gens:
                # move chip/gen pair up
                new_config = [[chip, gen] for chip, gen in cur_config]
                new_config[chip1][0] += 1
                new_config[chip1][1] += 1
                new_config.sort()
                if isValid(new_config) and (new_config, elevator+1) not in visited:
                    moves.append((new_config, elevator+1, steps+1))
                    visited.append((new_config, elevator+1))
                # move chip/gen pair down
                new_config = [[chip, gen] for chip, gen in cur_config]
                new_config[chip1][0] -= 1
                new_config[chip1][1] -= 1
                new_config.sort()
                if isValid(new_config) and (new_config, elevator-1) not in visited:
                    moves.append((new_config, elevator-1, steps+1))
                    visited.append((new_config, elevator-1))
        for i, gen1 in enumerate(gens):
            # move gen up
            new_config = [[chip, gen] for chip, gen in cur_config]
            new_config[gen1][1] += 1
            new_config.sort()
            if isValid(new_config) and (new_config, elevator+1) not in visited:
                moves.append((new_config, elevator+1, steps+1))
                visited.append((new_config, elevator+1))
            # move gen down
            new_config = [[chip, gen] for chip, gen in cur_config]
            new_config[gen1][1] -= 1
            new_config.sort()
            if isValid(new_config) and (new_config, elevator-1) not in visited:
                moves.append((new_config, elevator-1, steps+1))
                visited.append((new_config, elevator-1))
            for gen2 in gens[i+1:]:
                # move pair up
                new_config = [[chip, gen] for chip, gen in cur_config]
                new_config[gen1][1] += 1
                new_config[gen2][1] += 1
                new_config.sort()
                if isValid(new_config) and (new_config, elevator+1) not in visited:
                    moves.append((new_config, elevator+1, steps+1))
                    visited.append((new_config, elevator+1))
                # move pair down
                new_config = [[chip, gen] for chip, gen in cur_config]
                new_config[gen1][1] -= 1
                new_config[gen2][1] -= 1
                new_config.sort()
                if isValid(new_config) and (new_config, elevator-1) not in visited:
                    moves.append((new_config, elevator-1, steps+1))
                    visited.append((new_config, elevator-1))


if __name__=="__main__":
    test_config = [[1,2], [1,3]]
    print findRoute(test_config) == 11

    # The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
    # The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
    # The third floor contains nothing relevant.
    # The fourth floor contains nothing relevant.

    print findRoute([[2,1], [1,1], [2,1], [1,1], [1,1]])

    print findRoute([[2,1], [1,1], [2,1], [1,1], [1,1], [1,1], [1,1]])
