def isValid(c):
    if ('0' <= c and c <= '9' ): return True
    if ('A' <= c and c <= 'Z'): return True
    if ('a' <= c and c <= 'z'): return True
    if ('.' == c or c == '_' or c == '-'): return True
    return False

line = "dana@dansid.com> "
for i in range(len(line)):
    if(line[i] == '@'):
        hasDot = False
        for s in range (i -1, -1, -1):
            if not isValid(line[s]):
                break
        if not isValid(line[s]): s += 1
        for e in range(i + 1, len(line)):
            if not isValid(line[e]):
                break
            if line[e] == '.': hasDot = True
        if isValid(line[e]): e += 1
        print(s, e, hasDot, line[s:e])

