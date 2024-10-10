
for _ in range(int(input())):
    n = int(input())
    x, y = list(map(int, input().split()))
    ans = n // min(x, y)
    if n % min(x, y): ans += 1
    print(ans)