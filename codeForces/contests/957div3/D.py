
for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    s = input()
    pos = -1
    while pos < n:
        i = pos + 1
        croco = False
        # print("debug: ", pos, i)
        while i < n and s[i] != 'L' and i-pos < m:
            i += 1
            # print("Avança...", i, croco)
        if i == n:
            ans = True
            break
        elif s[i] == 'L':
            pos = i
            continue
        else:
            pos = i
            # Toca nedar
            while pos < n and s[pos] == 'W':
                pos += 1
                k -= 1
            if k < 0:
                ans = False
                break
            if pos >= n:
                ans = True
                break
            elif s[pos] == 'C':
                ans = False
                break
            else: # s[pos] == 'L'
                continue
    print("YES" if ans else "NO")