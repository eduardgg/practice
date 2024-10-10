
for _ in range(int(input())):
    s = input()
    uns = 0
    ans = 0
    for e in s:
        if e == '1':
            uns += 1
        elif uns:
            ans += (1+uns)
    print(ans)