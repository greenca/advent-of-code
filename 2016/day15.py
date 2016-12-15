def dropSuccess(t, num_position, start_positions):
    for i in range(len(num_positions)):
        disc_position = ((t + i + 1) + start_position[i]) % num_positions[i]
        if disc_position != 0:
            return False
    return True

def findDropTime(num_positions, start_position):
    t = 0
    while True:
        if dropSuccess(t, num_positions, start_position):
            return t
        t += 1

if __name__=="__main__":
    num_positions = [7, 13, 3, 5, 17, 19]
    start_position = [0, 0, 2, 2, 0, 7]
    print findDropTime(num_positions, start_position)
    num_positions.append(11)
    start_position.append(0)
    print findDropTime(num_positions, start_position)
