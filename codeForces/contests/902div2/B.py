t = int(input())
for _ in range(t):
    n, p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    n -= 1
    cost = p
    costos = [(b[i], a[i]) for i in range(len(a))] + [(p, float('inf'))]
    costos.sort()
    for (b, a) in costos:
        if n <= 0:
            break
        cost += b*min(n, a)
        n -= a
    
    print(cost)