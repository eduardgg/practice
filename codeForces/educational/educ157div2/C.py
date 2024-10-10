
n = int(input())
a = input().split()
suma = [0]*n
dp = {}

for i in range(n):
    for e in a[i]:
        suma[i] += int(e)
    tup = (len(a[i]), suma[i])
    dp[tup] = dp.get(tup, 0) + 1 

ans = 0
for i in range(n):
    ans += dp.get((len(a[i]), suma[i]), 0) # Si medeix igual que a[i]
    for lt in range(len(a[i])+2-len(a[i])%2, 2*len(a[i]), 2): # a[i] és la part llarga
        suml = 2*sum([int(a[i][k]) for k in range(min(lt//2, len(a[i])))]) - suma[i]
        sumr = suma[i] - 2*sum([int(a[i][k]) for k in range(len(a[i])-lt//2)])
        ans += dp.get((lt - len(a[i]), suml), 0)   # a[i] va a l'esquerra
        ans += dp.get((lt - len(a[i]), sumr), 0)   # a[i] va a la dreta

print(ans)