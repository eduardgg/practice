
line = lambda : list(map(int, input().split()))
mod = 998244353
n, q = line()
gold = [0] + line()
silver = [0] + line()
for i in range(n):
    gold[i+1] += gold[i]
    silver[i+1] += silver[i]
tg = gold[-1]
ts = silver[-1]

bin = [0, 1]
for i in range(ts):
    bin.append(bin[-1] * (ts-i) * pow(i+1,-1,mod) % mod)
for i in range(ts+1):
    bin[i+1] += bin[i]

for i in range(q):
    l, r = line()
    g = gold[r] - gold[l-1]
    s = silver[r] - silver[l-1]
    v = 2*g+s-tg
    if v < 0:
        print(0)
    elif v > ts:
        print(1)
    else:
        print(bin[v] * pow(2,-ts,mod) % mod)