
for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    suma = 0
    j = 0
    fin = []
    for i in range(n):
        while suma <= x and j < n:
            suma += a[j]
            j += 1
        if suma <= x:
            fin.append(j)
        else:
            fin.append(j-1)
        suma -= a[i]
    
    dp = [0]*(n+2)
    for j in range(n-1, -1, -1):
        if fin[j] < n:
            dp[j] += 1
        dp[j] += dp[fin[j]+1]

    ans = n*(n+1)//2 - sum(dp)
    print(ans)