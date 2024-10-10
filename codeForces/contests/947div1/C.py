
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    v = [(a[i], i) for i in range(n)]
    v.sort(reverse=True)
    vist = [False]*(n+1)
    for (e, i) in v:
        vist[i] = True
        if (i-2 >= 0 and vist[i-2]) or (i-1 >= 0 and vist[i-1]) or (i+1 <= n and vist[i+1]) or (i+2 <= n and vist[i+2]):
            print(e)
            break