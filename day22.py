import random

num_trials = 10000

boss_hit = 55
boss_damage = 8

my_hit = 50
my_mana = 500

spells = [
{'name': 'Magic Missile', 'turns': 0, 'cost': 53, 'damage': 4, 'heal': 0, 'armor': 0, 'mana': 0},
{'name': 'Drain', 'turns': 0, 'cost': 73, 'damage': 2, 'heal': 2, 'armor': 0, 'mana': 0},
{'name': 'Shield', 'turns': 6, 'cost': 113, 'damage': 0, 'heal': 0, 'armor': 7, 'mana': 0},
{'name': 'Poison', 'turns': 6, 'cost': 173, 'damage': 3, 'heal': 0, 'armor': 0, 'mana': 0},
{'name': 'Recharge', 'turns': 5, 'cost': 229, 'damage': 0, 'heal': 0, 'armor': 0, 'mana': 101} ]


win_costs = []
loss_costs = []

for i in range(num_trials):
    total_cost = 0
    b_hit = boss_hit
    cur_hit = my_hit
    cur_mana = my_mana
    effects = {}
    player = 0

    while b_hit > 0 and cur_hit > 0:
        if player == 0:
            cur_hit -= 1

        if cur_hit <= 0:
            break

        cur_armor = 0
        expired_effects = []
        for name in effects:
            effect = effects[name][1]
            remaining = effects[name][0]

            b_hit -= effect['damage']
            cur_armor += effect['armor']
            cur_mana += effect['mana']

            if remaining == 1:
                expired_effects.append(name)
            else:
                effects[name][0] = remaining - 1

        for name in expired_effects:
            del effects[name]

        if player == 0:
            if min([spell['cost'] for spell in spells if spell['name'] not in effects]) > cur_mana:
                cur_hit = 0
                break
            spell = random.choice([spell for spell in spells if spell['cost'] <= cur_mana and spell['name'] not in effects])
            cur_mana -= spell['cost']
            total_cost += spell['cost']
            if spell['turns'] == 0:
                b_hit -= spell['damage']
                cur_hit += spell['heal']
            else:
                effects[spell['name']] = [spell['turns'], spell]
            player = 1

        else:
            cur_hit -= max(1, boss_damage-cur_armor)
            player = 0

    if cur_hit > 0:
        win_costs.append(total_cost)


print min(win_costs)


