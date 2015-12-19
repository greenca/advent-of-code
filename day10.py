# input = '1'
input = '1113222113'

for i in range(50):

    prev_char = ''
    rep_num = 0
    output = ''

    for c in input:
        if c == prev_char:
            rep_num += 1
        else:
            if rep_num > 0:
                output += str(rep_num) + prev_char
            prev_char = c
            rep_num = 1

    output += str(rep_num) + prev_char

    # print output

    input = output

print len(output)
