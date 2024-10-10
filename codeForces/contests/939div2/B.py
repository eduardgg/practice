
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    ans = 0
    s = set()
    for e in a:
        if e in s:
            ans += 1
        else:
            s.add(e)
    print(ans)