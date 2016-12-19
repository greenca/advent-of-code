import math

class Elf:
    def __init__(self, id):
        self.id = id
        self.next = None
        self.prev = None

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev


def stealGifts(num_elves):
    elves = map(Elf, xrange(num_elves))
    for i in xrange(num_elves):
        elves[i].next = elves[(i+1) % num_elves]
        elves[i].prev = elves[(i-1) % num_elves]
    
    cur_elf = elves[0]
    while cur_elf != cur_elf.next:
        cur_elf.next.delete()
        cur_elf = cur_elf.next

    return cur_elf.id + 1

def stealAcross(num_elves):
    elves = map(Elf, xrange(num_elves))
    for i in xrange(num_elves):
        elves[i].next = elves[(i+1) % num_elves]
        elves[i].prev = elves[(i-1) % num_elves]

    cur_elf = elves[0]
    cross_elf = elves[num_elves/2]

    for i in xrange(num_elves-1):
        cross_elf.delete()
        cross_elf = cross_elf.next
        if (num_elves-i) % 2 == 1:
            cross_elf = cross_elf.next
        cur_elf = cur_elf.next
    
    return cur_elf.id + 1


if __name__=="__main__":
    print stealGifts(5) == 3
    num_elves = 3014603
    print stealGifts(num_elves)
    print stealAcross(5) == 2
    print stealAcross(num_elves)
