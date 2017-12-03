sum = 0
with open('day2_input.txt') as f:
    for row in f:
        numbers = map(int, row.split())
        sum += max(numbers) - min(numbers)
print sum


sum = 0
with open('day2_input.txt') as f:
    for row in f:
        numbers = map(int, row.split())
        for i, n in enumerate(numbers):
            for m in numbers[i+1:]:
                if n % m == 0:
                    sum += n/m
                elif m % n == 0:
                    sum += m/n
print sum
