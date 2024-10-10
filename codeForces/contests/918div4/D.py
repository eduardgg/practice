
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    vows = {'a', 'e'}
    cons = {'b', 'c', 'd'}
    cs = 0
    syl = ''
    for i in range(len(s)-1):
        syl += s[i]
        if len(syl) == 1:
            continue
        elif len(syl) == 2:
            if i+2 < len(s) and s[i+2] in vows:
                print(syl, end='.')
                syl = ''
            else:
                continue
        if len(syl) == 3:
            print(syl, end=".")
            syl = ''
    syl += s[-1]
    print(syl)