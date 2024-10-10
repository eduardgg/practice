
from bisect import bisect_left
v = [9]
for i in range(1, 20):
    v.append(v[-1] + (i+1)*9*(10**i))

for i in range(int(input())):
    n = int(input())
    i = bisect_left(v, n)
    if i == 0:
        print(n)
        continue
    if n == v[i]:
        print(9)
        continue
    a = (n-v[i-1]-1)//(i+1)
    res = (n-v[i-1])%(i+1)
    if res: res = (i+1)-res
    ans = ((10**i + a) // (10**res)) % 10
    print(ans)