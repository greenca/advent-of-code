import hashlib

# input = 'abcdef'
# input = 'pqrstuv'
input = 'yzbqklnj'

found = False
i = 0

while not found:
    i += 1
    output = hashlib.md5(input + str(i)).hexdigest()
    if output[:6] == '000000':
        found = True

print i
