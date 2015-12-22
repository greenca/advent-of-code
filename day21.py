import itertools

# Boss stats
boss_hit = 100
boss_damage = 8
boss_armor = 2

my_hit = 100

# Weapons:    Cost  Damage  Armor
weapons = [
['Dagger',        8,     4,       0],
['Shortsword',   10,     5,       0],
['Warhammer',    25,     6,       0],
['Longsword',    40,     7,       0],
['Greataxe',     74,     8,       0]]

# Armor:      Cost  Damage  Armor
armors = [
['Leather',      13,     0,       1],
['Chainmail',    31,     0,       2],
['Splintmail',   53,     0,       3],
['Bandedmail',   75,     0,       4],
['Platemail',   102,     0,       5]]

# Rings:      Cost  Damage  Armor
rings = [
['Damage +1',    25,     1,       0],
['Damage +2',    50,     2,       0],
['Damage +3',   100,     3,       0],
['Defense +1',   20,     0,       1],
['Defense +2',   40,     0,       2],
['Defense +3',   80,     0,       3]]


win_costs = []
lose_costs = []
for weapon in weapons:
    for armor in armors:
        for num_armor in range(2):
            for num_rings in range(3):
                for ring_group in itertools.combinations(rings,num_rings):
                    cost = weapon[1]
                    my_damage = weapon[2]
                    my_armor = weapon[3]
                    if num_armor == 1:
                        cost += armor[1]
                        my_damage += armor[2]
                        my_armor += armor[3]
                    for ring in ring_group:
                        cost += ring[1]
                        my_damage += ring[2]
                        my_armor += ring[3]
                    hit = my_hit
                    b_hit = boss_hit
                    while hit > 0 and b_hit > 0:
                        b_hit -= max(1, my_damage - boss_armor)
                        if b_hit <= 0:
                            break
                        hit -= max(1, boss_damage - my_armor)
                    if hit > 0:
                        win_costs.append(cost)
                    else:
                        lose_costs.append(cost)

print min(win_costs)
print max(lose_costs)
