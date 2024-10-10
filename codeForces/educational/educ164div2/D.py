
mod = 998244353
n = int(input())
a = list(map(int, input().split()))
a.sort()

suma = 0
q = {0: 1}

for i in range(n):

    cnt = 0
    for k in q.keys():
        if k > a[i]:
            suma = (suma + (k+a[i]+1)//2 * q[k]) % mod
        else:
            cnt += q[k]
    suma = (suma + cnt*a[i]) % mod

    qk = [(k, q[k]) for k in q.keys()]
    for (k, qu) in qk:
        q[k+a[i]] = (q.get(k+a[i], 0) + qu) % mod
    

print(suma)