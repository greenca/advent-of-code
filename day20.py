num_gifts = 36000000
house = [0 for j in range(num_gifts/10)]
house_limited = [0 for j in range(num_gifts/10)]

for i in range(1, num_gifts/10):
    for j in range(i, num_gifts/10, i):
        house[j] += i*10
    for j in range(i, min(50*i+1, num_gifts/10), i):
        house_limited[j] += i*11
        

matches = [i for i in range(1, num_gifts/10) if house[i] >= num_gifts]
print min(matches)

matches_lim = [i for i in range(1, num_gifts/10) if house_limited[i] >= num_gifts]
print min(matches_lim)
