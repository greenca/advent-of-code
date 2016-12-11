def init():
    bots = {}
    rules = {}
    outputs = {}
    return bots, rules, outputs

def parseInstr(instr, bots, rules):
    instr_vec = instr.split()
    if instr_vec[0] == "value":
        val = instr_vec[1]
        bot = instr_vec[5]
        bots = assignVal(bot, val, bots)
    else:
        bot = instr_vec[1]
        low_type = instr_vec[5]
        low_num = instr_vec[6]
        high_type = instr_vec[10]
        high_num = instr_vec[11]
        rules = assignRule(bot, low_type, low_num, high_type, high_num, rules)
    return bots, rules

def assignVal(bot, val, bots):
    bots[bot] = bots.get(bot,[]) + [int(val)]
    return bots

def assignRule(bot, low_type, low_num, high_type, high_num, rules):
    rules[bot] = {}
    rules[bot]['low'] = {'type': low_type, 'num': low_num}
    rules[bot]['high'] = {'type': high_type, 'num': high_num}
    return rules

def applyRule(bot, bots, rules, outputs):
    low_val = min(bots[bot])
    high_val = max(bots[bot])
    if low_val == 17 and high_val == 61:
        print bot
    low_dest = rules[bot]['low']['num']
    high_dest = rules[bot]['high']['num']
    if rules[bot]['low']['type'] == 'output':
        outputs[low_dest] = outputs.get(low_dest,[]) + [low_val]
    else:
        bots[low_dest] = bots.get(low_dest,[]) + [low_val]
    if rules[bot]['high']['type'] == 'output':
        outputs[high_dest] = outputs.get(high_dest,[]) + [high_val]
    else:
        bots[high_dest] = bots.get(high_dest,[]) + [high_val]
    bots[bot] = []
    return bots, rules, outputs

def runBots(bots, rules, outputs):
    while max(map(len, bots.values())) > 1:
        for bot in bots.keys():
            if len(bots[bot]) == 2:
                bots, rules, outputs = applyRule(bot, bots, rules, outputs)
    return bots, rules, outputs

if __name__=="__main__":
    bots, rules, outputs = init()
    with open("day10_test.txt") as f:
        for instr in f:
            bots, rules = parseInstr(instr, bots, rules)
    bots, rules, outputs = runBots(bots, rules, outputs)
    print outputs == {'0': [5], '1': [2], '2': [3]}

    bots, rules, outputs = init()
    with open("day10_input.txt") as f:
        for instr in f:
            bots, rules = parseInstr(instr, bots, rules)
    bots, rules, outputs = runBots(bots, rules, outputs)
    print outputs['0'][0]*outputs['1'][0]*outputs['2'][0]
