
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    k, q = line()
    a = line()
    n = line()
    ans = []
    for i in n:
        ans.append(min(a[0]-1, i))
    print(*ans)