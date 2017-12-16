def CrossFirewall(filename):

    firewall = {}
    with open(filename) as f:
        for row in f:
            layer_depth, scanning_range = map(int, row.split(": "))
            firewall[layer_depth] = {'range': scanning_range, 'pos': 0, 'dir': 1}

    severity = 0
    packet_layer = 0
    while packet_layer <= max(firewall):
        if packet_layer in firewall:
            if firewall[packet_layer]['pos'] == 0:
                severity += packet_layer*firewall[packet_layer]['range']
        for k in firewall:
            if firewall[k]['pos'] == 0:
                firewall[k]['dir'] = 1
            elif firewall[k]['pos'] == firewall[k]['range']-1:
                firewall[k]['dir'] = -1
            firewall[k]['pos'] += firewall[k]['dir']
        packet_layer += 1

    return severity


print CrossFirewall("day13_test.txt") == 24
print CrossFirewall("day13_input.txt")


def CanCrossFirewall(firewall, start_delay):
    for k in firewall:
        if (start_delay + k) % (2*(firewall[k]-1)) == 0:
            return False
    return True


def DelayFirewall(filename):
    firewall = {}
    with open(filename) as f:
        for row in f:
            layer_depth, scanning_range = map(int, row.split(": "))
            firewall[layer_depth] = scanning_range

    start_delay = 0
    success = CanCrossFirewall(firewall, start_delay)
    while not success:
        start_delay += 1
        success = CanCrossFirewall(firewall, start_delay)
    return start_delay

    
print DelayFirewall("day13_test.txt") == 10
print DelayFirewall("day13_input.txt")
