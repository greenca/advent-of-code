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

spells_cast = ['Poison', '', 'Recharge', '', 'Shield', '', 'Magic Missile', '', 'Poison', '', 'Magic Missile', '', 'Magic Missile', '', 'Magic Missile', '']

total_cost = 0
b_hit = boss_hit
cur_hit = my_hit
cur_mana = my_mana
effects = {}
player = 0

for spell_name in spells_cast:
    print 'Initial',b_hit,cur_hit,cur_mana
    #print effects
    #print spell_name in effects
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
        print 'Player Turn'
        if min([spell['cost'] for spell in spells if spell['name'] not in effects]) > cur_mana:
            cur_hit = 0
            break
        spell = [spell for spell in spells if spell['name'] == spell_name][0]
        print spell['name']

        cur_mana -= spell['cost']
        total_cost += spell['cost']
        if spell['turns'] == 0:
            b_hit -= spell['damage']
            cur_hit += spell['heal']
        else:
            effects[spell['name']] = [spell['turns'], spell]
        player = 1

    else:
        print 'Boss Turn'
        cur_hit -= max(1, boss_damage-cur_armor)
        player = 0

    print 'Final',b_hit,cur_hit,cur_mana

