
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    maxim = 0
    for c in s:
        d[c] = d.get(c, 0) + 1
        maxim = max(maxim, d[c])
    print(max(n%2, 2*maxim-n))