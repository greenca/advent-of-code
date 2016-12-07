from collections import Counter

def errorCorrect(messages):
    msg_chars = []
    for msg in messages:
        if not msg_chars:
            msg_chars = list(msg.strip())
        else:
            for i, c in enumerate(msg.strip()):
                msg_chars[i] += c
    output = ''
    for chars in msg_chars:
        output += Counter(chars).most_common(1)[0][0]
    return output

def errorCorrectMod(messages):
    msg_chars = []
    for msg in messages:
        if not msg_chars:
            msg_chars = list(msg.strip())
        else:
            for i, c in enumerate(msg.strip()):
                msg_chars[i] += c
    output = ''
    for chars in msg_chars:
        output += Counter(chars).most_common()[-1][0]
    return output


testMessages = ['eedadn',
'drvtee',
'eandsr',
'raavrd',
'atevrs',
'tsrnev',
'sdttsa',
'rasrtv',
'nssdts',
'ntnada',
'svetve',
'tesnvt',
'vntsnd',
'vrdear',
'dvrsen',
'enarar']

if __name__=="__main__":
    print errorCorrect(testMessages) == "easter"
    print errorCorrectMod(testMessages) == "advent"
    with open("day6_input.txt") as f:
        messages = list(f)
        print errorCorrect(messages)
        print errorCorrectMod(messages)


