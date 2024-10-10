
for _ in range(int(input())):
    x, y, k = list(map(int, input().split()))

    while k and x >= y:
        inc = min(k, y - (x%y))
        x += inc
        k -= inc
        while not x%y:
            x //= y
    if k:
        k %= y-1
        x += k
        if x >= y:
            x = 1 + (x-y)
    
    print(x)