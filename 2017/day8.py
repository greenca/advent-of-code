registers = {}
running_max = 0

with open('day8_input.txt') as f:
    for row in f:
        items = row.split()
        target = registers.get(items[4], 0)
        cond = eval('target' + items[5] + items[6])
        old_val = registers.get(items[0],0)
        if cond:
            if items[1] == 'inc':
                new_val = old_val + int(items[2])
            else:
                new_val = old_val - int(items[2])
            registers[items[0]] = new_val
            if new_val > running_max:
                running_max = new_val

            
print max(registers.values())
print running_max
