t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    i = 2
    isOrdered = True
    while i < len(v):
        for j in range(i+1, min(2*i, len(v))):
            if v[j] < v[j-1]:
                isOrdered = False
                break
        if not isOrdered:
            print("NO")
            break
        i *= 2
    if isOrdered:
        print("YES")