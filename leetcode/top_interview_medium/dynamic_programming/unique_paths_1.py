"""
from math import comb
def uniquePaths(m, n):
    return comb(n+m-2,n-1)
"""

def recursion(m, n, dp):
    if m == 1 or n == 1:
        return 1
    if dp[m-1][n-1] != -1:
        return dp[m-1][n-1]
    else:
        dp[m-1][n-1] = recursion(m-1,n,dp) + recursion(m,n-1,dp)
        return dp[m-1][n-1]

def uniquePaths(m, n):
    dp = [[-1 for i in range(n)] for j in range(m)]
    return recursion(m, n, dp)
     
print(uniquePaths(7,3))