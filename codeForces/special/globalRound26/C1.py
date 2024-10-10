
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [abs(a[0])]
    sumpos = [0]
    for e in a[::-1]:
        sumpos.append(sumpos[-1] + e)
    sumpos = sumpos[::-1]
    top = sumpos[0]
    cur = 0
    for i in range(n):
        cur += a[i]
        if a[i] < 0:
            top = max(top, sumpos[i+1] + abs(cur))
    print(top)