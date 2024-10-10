
for _ in range(int(input())):
    l, r = list(map(int, input().split()))
    ans = 0
    copy = l
    while copy:
        copy //= 3
        ans += 2
    
    i = 0
    while 3**i <= r:
        if 3**(i+1) >= l+1:
            ans += (min(3**(i+1), r+1) - max(3**i, l+1)) * (i+1)
        i += 1
    print(ans)