
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):

    s = input()
    s = s[::-1]
    ans = []
    bs, Bs = 0, 0
    for c in s:
        if c == 'b':
            bs += 1
        elif c == 'B':
            Bs += 1
        elif 0 <= ord(c)-ord('a') < 26:
            if bs:
                bs -= 1
            else:
                ans.append(c)
        else: # Majúscula
            if Bs:
                Bs -= 1
            else:
                ans.append(c)

    ans = ''.join(ans)
    print(ans[::-1])