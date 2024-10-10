
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    a = [1] + line()
    b = line()
    a.sort()
    b.sort()
    i, j = 0, 0
    rem = 0
    while j < n:
        if a[i] < b[j]:
            i += 1
            j += 1
        else:
            j += 1
            rem += 1
    print(rem)