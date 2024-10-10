
for _ in range(int(input())):
    x, y, z, V = list(map(int, input().split()))
    ans = 0
    for i in range(1, min(V, x) + 1):
        if V % i:
            continue
        for j in range(1, min(V//i, y) + 1):
            if (V // i) % j:
                continue
            k = V // (i*j)
            if k <= z:
                ans = max(ans, (x-i+1)*(y-j+1)*(z-k+1))
    print(ans)