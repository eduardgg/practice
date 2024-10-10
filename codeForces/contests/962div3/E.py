
mod = 10**9 + 7
for _ in range(int(input())):
    a = input()
    n = len(a)
    ans = 0
    acu = [1+i for i in range(n+1)]
    prefix = [0]
    last = {0:0}
    for i in range(n):
        prefix.append(prefix[-1]-1+2*int(a[i]))
        if prefix[-1] in last.keys():
            ans += acu[last[prefix[-1]]] * (n - i)
            acu[i+1] += acu[last[prefix[-1]]]
            ans %= mod
        last[prefix[-1]] = i+1
    print(ans)