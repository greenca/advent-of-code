def scoreGroups(stream):
    stream = removeCanceled(stream)
    stream = removeGarbage(stream)
    level = 0
    score = 0
    for c in stream:
        if c == "{":
            level += 1
        elif c == "}":
            score += level
            level -= 1
    return score

def removeCanceled(stream):
    newstream = ""
    while stream:
        c = stream[0]
        if c == "!":
            stream = stream[2:]
        else:
            newstream += c
            stream = stream[1:]
    return newstream

def removeGarbage(stream):
    newstream = ""
    while stream:
        c = stream[0]
        if c == "<":
            garbage_end = stream.index(">")
            stream = stream[garbage_end+1:]
        else:
            newstream += c
            stream = stream[1:]
    return newstream

def countGarbage(stream):
    stream = removeCanceled(stream)
    count = 0
    while stream:
        c = stream[0]
        if c == "<":
            garbage_end = stream.index(">")
            count += garbage_end - 1
            stream = stream[garbage_end+1:]
        else:
            stream = stream[1:]
    return count


print scoreGroups("{}") == 1
print scoreGroups("{{{}}}") == 6
print scoreGroups("{{},{}}") == 5
print scoreGroups("{{{},{},{{}}}}") == 16
print scoreGroups("{<a>,<a>,<a>,<a>}") == 1
print scoreGroups("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
print scoreGroups("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
print scoreGroups("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

with open("day9_input.txt") as f:
    input = f.read()
    print scoreGroups(input)


print countGarbage("<>") == 0
print countGarbage("<random characters>") == 17
print countGarbage("<<<<>") == 3
print countGarbage("<{!>}>") == 2
print countGarbage("<!!>") == 0
print countGarbage("<!!!>>") == 0
print countGarbage('<{o"i!a,<{i<a>') == 10

with open("day9_input.txt") as f:
    input = f.read()
    print countGarbage(input)
