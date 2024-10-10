
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    a = input()
    i = 0
    while i < len(a) and a[i] == 0:
        i += 1
    ans = 1
    i += 1
    ok = True
    while i < len(a):
        if a[i] != a[i-1]:
            ans += 1
            if ok and a[i] == '1':
                ok = False
                ans -= 1
        i += 1
    print(ans)