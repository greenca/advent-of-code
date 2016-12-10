def initScreen(width=50, height=6):
    return [[0 for i in range(width)] for j in range(height)]

def executeInstruction(screen, instr):
    components = instr.split()
    if components[0] == "rect":
        width, height = map(int, components[1].split('x'))
        return addRectangle(screen, width, height)
    elif components[0] == "rotate":
        if components[1] == "row":
            row = int(components[2].split('=')[1])
            amount = int(components[4])
            return shiftRow(screen, row, amount)
        elif components[1] == "column":
            col = int(components[2].split('=')[1])
            amount = int(components[4])
            return shiftCol(screen, col, amount)

def addRectangle(screen, width, height):
    for i in range(height):
        for j in range(width):
            screen[i][j] = 1
    return screen

def shiftRow(screen, row, amount):
    original = screen[row]
    screen[row] = original[len(original)-amount:] + original[:len(original)-amount]
    return screen

def shiftCol(screen, col, amount):
    original = [screen_row[col] for screen_row in screen]
    new_col = original[len(original)-amount:] + original[:len(original)-amount]
    for i, screen_row in enumerate(screen):
        screen_row[col] = new_col[i]
    return screen


if __name__=="__main__":
    screen = initScreen(7,3)
    screen = executeInstruction(screen, "rect 3x2")
    print screen == [[1,1,1,0,0,0,0], [1,1,1,0,0,0,0], [0,0,0,0,0,0,0]]
    screen = executeInstruction(screen, "rotate column x=1 by 1")
    print screen == [[1,0,1,0,0,0,0], [1,1,1,0,0,0,0], [0,1,0,0,0,0,0]]
    screen = executeInstruction(screen, "rotate row y=0 by 4")
    print screen == [[0,0,0,0,1,0,1], [1,1,1,0,0,0,0], [0,1,0,0,0,0,0]]
    screen = executeInstruction(screen, "rotate column x=1 by 1")
    print screen == [[0,1,0,0,1,0,1], [1,0,1,0,0,0,0], [0,1,0,0,0,0,0]]

    screen = initScreen()
    with open("day8_input.txt") as f:
        for instr in f:
            screen = executeInstruction(screen, instr)
    print sum([sum(row) for row in screen])

    def convert(x):
        if x:
            return '#'
        else:
            return ' '

    screen_display = '\n'.join([''.join(map(convert, row)) for row in screen])
    print screen_display

