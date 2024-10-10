
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[-1] - a[-2] + sum(a[:n-2])
    print(ans)