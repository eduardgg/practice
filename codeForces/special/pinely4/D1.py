
N = 2001
primes = []
isprime = [True] * N
for i in range(2, N):
    if not isprime[i]:
        continue
    primes.append(i)
    for j in range(i*2, N, i):
        isprime[j] = False

used = set()
ans = [len(used)]
color = [-1]*N
for i in range(1, N):
    prohibit = set()
    for p in primes:
        if p ^ i < N:
            prohibit.add(color[p ^ i])
    c = 1
    while c in prohibit:
        c += 1
    color[i] = c
    used.add(c)
    ans.append(len(used))


for _ in range(int(input())):
    n = int(input())
    print(ans[n])
    print(*color[1:n+1])