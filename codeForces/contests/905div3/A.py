
for _ in range(int(input())):
    s = input()
    pos = 1
    ans = 4
    for c in s:
        c = int(c)
        if c == 0: c += 10
        ans += max(pos-c, c-pos)
        pos = c
    print(ans)