
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    s = [e for e in input()]
    ind = list(set(map(int, input().split())))
    c = [e for e in input()]
    ind.sort()
    c.sort(reverse=True)
    for e in ind:
        s[e-1] = c.pop()
    print(''.join(s))