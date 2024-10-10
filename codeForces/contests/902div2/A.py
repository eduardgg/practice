t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    print(-sum(v))