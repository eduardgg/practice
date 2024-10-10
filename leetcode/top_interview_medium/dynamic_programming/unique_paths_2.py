def uniquePaths(m, n):
    dp = [[0 for i in range(n)] for j in range(m)]
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        dp[i][0] = 1
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
     
print(uniquePaths(7,3))