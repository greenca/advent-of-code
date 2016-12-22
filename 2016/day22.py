import re
import collections

def viablePairs(disk_usage):
    all_disks = []
    for disk in disk_usage:
        name, size, used, avail, perc = disk.strip().split()
        all_disks.append({'name': name, 'size': int(size[:-1]), 'used': int(used[:-1]), 'avail': int(avail[:-1]), 'perc': perc})
    viable = []
    for i, disk1 in enumerate(all_disks):
        for j, disk2 in enumerate(all_disks[i+1:]):
            if disk1['used'] != 0 and disk1['used'] <= disk2['avail']:
                viable.append((i, i+1+j))
            if disk2['used'] != 0 and disk2['used'] <= disk1['avail']:
                viable.append((i+1+j, i))
    return viable

def printArray(disk_usage):
    disks = {}
    max_x = 0
    max_y = 0
    for disk in disk_usage:
        name, size, used, avail, perc = disk.strip().split()
        match = re.search(r'(\d+)\D+(\d+)', name)
        x = int(match.group(1))
        y = int(match.group(2))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        disks[(x,y)] = {'size': int(size[:-1]), 'used': int(used[:-1]), 'avail': int(avail[:-1]), 'perc': perc}
    disk_array = [[str(disks[(x,y)]['used']) + '/' + str(disks[(x,y)]['avail']) for y in range(max_y+1)] for x in range(max_x+1)] 
    for row in disk_array:
        print '\t'.join(row)


if __name__=="__main__":
    with open("day22_input.txt") as f:
        disk_usage = list(f)
        disk_usage = disk_usage[2:]
        print len(viablePairs(disk_usage))
        print viablePairs(disk_usage)
        printArray(disk_usage)
