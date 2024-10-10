
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    sumes = [0]
    for e in a: sumes.append(sumes[-1] + e)
    ans = 0
    l, r = 0, n-1
    while l < r:
        if s[l] == 'R':
            l += 1
            continue
        if s[r] == 'L':
            r -= 1
            continue
        ans += sumes[r+1] - sumes[l]
        l += 1
        r -=1
    print(ans)