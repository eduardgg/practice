import time
def recursion(coins, amount, dp):
    if dp[amount] != -2:
        return dp[amount]
    for c in coins:
        if amount < c:
            continue
            # Si els coins estiguessin ordenats, podríem usar "break"
        if dp[amount-c] == -2:
            dp[amount-c] = recursion(coins,amount-c,dp)
    if max([-1]+[dp[amount-c] for c in coins if amount >= c]) == -1:
        dp[amount-c] = -1
        return dp[amount-c]
    dp[amount-c] = 1 + min(dp[amount-c] for c in coins if dp[amount-c] >= 0)
    return dp[amount-c]

def coinChange(coins, amount):
    # -2 significa desconegut, -1 significa impossible
    dp = [0] + [-2 for i in range(amount)]
    return recursion(coins, amount, dp)

coins = [1,2,5]
amount = 11
print(coinChange(coins,amount))

coins = [2]
amount = 3
print(coinChange(coins,amount))

coins = [1]
amount = 0
print(coinChange(coins,amount))

coins = [1]
amount = 1
print(coinChange(coins,amount))

coins = [1]
amount = 2
print(coinChange(coins,amount))

coins = [474,83,404,3]
amount = 264
print(coinChange(coins,amount))

start = time.time()
coins = [4,12,19,39,139,294,892]
amount = 1282
print(coinChange(coins,amount))
end = time.time()
print(end - start)