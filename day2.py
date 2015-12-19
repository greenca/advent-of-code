total_area = 0
total_ribon = 0

with open("day2_input.txt") as f:
    for present in f:
        sides = [int(side) for side in present.strip().split('x')]
        sides.sort()
        area = 3*sides[0]*sides[1] + 2*sides[0]*sides[2] + 2*sides[1]*sides[2]
        ribon = 2*sides[0] + 2*sides[1] + sides[0]*sides[1]*sides[2]
        total_area += area
        total_ribon += ribon

print total_area
print total_ribon
