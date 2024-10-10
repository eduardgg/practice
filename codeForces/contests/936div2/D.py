
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, x = line()
    a = line()
    xor = 0
    for e in a:
        xor ^= e
    if xor > x:
        print(-1)
        continue
    xori = 0
    ans = 1
    for e in a[:-1]:
        xori ^= e
        if (xor ^ xori) | xori <= x:
            ans += 1
            xori = 0
            xor ^= xori
    
    print(ans)
