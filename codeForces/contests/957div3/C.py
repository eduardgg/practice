
for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    ans = [i for i in range(n, k-1, -1)] + [i for i in range(m+1, k)] + [i for i in range(1, m+1)]
    print(*ans)