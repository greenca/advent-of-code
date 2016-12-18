def findSafeTiles(first_row, num_rows):
    num_cols = len(first_row)
    cur_row = first_row
    num_safe = cur_row.count('.')
    for i in range(1, num_rows):
        prev_row = cur_row
        cur_row = ''
        for j in range(num_cols):
            if j > 0:
                left = prev_row[j-1]
            else:
                left = '.'
            if j < num_cols-1:
                right = prev_row[j+1]
            else:
                right = '.'
            if (left == '^') != (right == '^'):
                cur_row += '^'
            else:
                cur_row += '.'
                num_safe += 1
    return num_safe


if __name__=="__main__":
    print findSafeTiles('..^^.', 3) == 6
    print findSafeTiles('.^^.^.^^^^', 10) == 38

    first_row = "^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^......."
    print findSafeTiles(first_row, 40)
    print findSafeTiles(first_row, 400000)
