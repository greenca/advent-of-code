code_chars = 0
mem_chars = 0
enc_chars = 0

with open("day8_input.txt") as f:
    for s in f:
        c_str = s.strip()
        code_chars += len(c_str)
        m_str = c_str.strip('"')
        i = 0
        while i < len(m_str):
            mem_chars += 1
            c = m_str[i]
            if c == '\\' and i < len(m_str)-1:
                if m_str[i+1] == '"' or m_str[i+1] == '\\':
                    i += 2
                elif m_str[i+1] == 'x':
                    i += 4
            else:
                i += 1
        for c in c_str:
            enc_chars += 1
            if c == '\\' or c == '"':
                enc_chars += 1
        enc_chars += 2

print code_chars
print mem_chars
print code_chars - mem_chars

print enc_chars
print enc_chars - code_chars
