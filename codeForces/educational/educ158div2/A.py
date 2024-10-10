t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    maxFuel = a[0]
    for i in range(len(a)-1):
        maxFuel = max(maxFuel, a[i+1]-a[i])
    maxFuel = max(maxFuel, 2*(x-a[-1]))
    print(maxFuel)