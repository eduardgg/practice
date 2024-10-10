
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    a = line()
    b = line()
    ans = 0
    i, j = n-1, n-1
    while i >= 0:
        if a[i] <= b[j]:
            i -= 1
            j -= 1
            continue
        i -= 1
        ans += 1
    print(ans)