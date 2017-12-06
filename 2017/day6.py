def reallocate(initial):
    previous_states = []

    cur = initial
    while cur not in previous_states:
        previous_states.append(cur)
        target = cur.index(max(cur))
        blocks = cur[target]
        new_state = [bank for bank in cur]
        new_state[target] = 0
        while blocks > 0:
            target = (target + 1) % len(new_state)
            new_state[target] += 1
            blocks -= 1
        cur = new_state

    return len(previous_states)

print reallocate([0, 2, 7, 0]) == 5
print reallocate([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3])


def loopSize(initial):
    previous_states = []

    cur = initial
    while cur not in previous_states:
        previous_states.append(cur)
        target = cur.index(max(cur))
        blocks = cur[target]
        new_state = [bank for bank in cur]
        new_state[target] = 0
        while blocks > 0:
            target = (target + 1) % len(new_state)
            new_state[target] += 1
            blocks -= 1
        cur = new_state

    return len(previous_states) - previous_states.index(cur)

print loopSize([0, 2, 7, 0]) == 4
print loopSize([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3])
