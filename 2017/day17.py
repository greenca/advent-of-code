def Spinlock(stepsize):
    circular_buffer = [0]
    cur_pos = 0
    for i in range(1, 2018):
        circular_buffer.insert((cur_pos + stepsize + 1) % len(circular_buffer), i)
        cur_pos = circular_buffer.index(i)
    return circular_buffer[(cur_pos + 1) % len(circular_buffer)]


print Spinlock(3) == 638
print Spinlock(348)


def FasterSpinlock(stepsize):
    buf_len = 1
    cur_pos = 0
    neighbour = None
    for i in xrange(1, 50000000):
        insert_after = (cur_pos + stepsize) % buf_len
        if insert_after == 0:
            neighbour = i
        buf_len += 1
        cur_pos = (insert_after + 1) % buf_len
    return neighbour


print FasterSpinlock(348)
