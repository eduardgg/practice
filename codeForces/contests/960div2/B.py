
for _ in range(int(input())):
    n, x, y = list(map(int, input().split()))
    a = [1 if (i+y)%2 else -1 for i in range(y-1)] + [1]*(x-y+1) + [1 if i%2 else -1 for i in range(n-x)]
    print(*a)