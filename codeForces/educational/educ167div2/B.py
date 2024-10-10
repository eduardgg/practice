
for _ in range(int(input())):
    a = input()
    b = input()
    ans = len(a)
    best = len(a) + len(b)
    for j in range(len(b)):
        i = 0
        k = j
        cur = len(a) + j
        while i < len(a) and k < len(b):
            if b[k] == a[i]:
                k += 1
            i += 1
        cur += len(b)-k
        best = min(best, cur)
    print(best)