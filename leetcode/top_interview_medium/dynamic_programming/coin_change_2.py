import time
def coinChange(coins, amount):
    if amount == 0:
        return 0
    dp = [0] + [-1 for i in range(amount)]
    stack = [0]
    while len(stack) > 0:
        s = len(stack)
        for i in range(s):
            e = stack.pop(0)
            for i in coins:
                if e+i >= amount:
                    if e+i == amount:
                        return dp[e]+1
                    continue
                if dp[e+i] >= 0:
                    continue
                dp[e+i] = dp[e]+1
                stack.append(e+i)
    return -1

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

coins = [1,3,5]
amount = 94
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