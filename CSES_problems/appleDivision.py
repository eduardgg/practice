
from bisect import bisect_left as bl

n = int(input())
p = list(map(int, input().split()))
sp = sum(p)
obj = sp/2
cjt = {0}

for e in p:
    for k in list(cjt):
        if k < obj and e+k not in cjt:
            cjt.add(e+k)

ans = sp
for e in cjt:
    if 2*e <= sp:
        ans = min(ans, sp-2*e)

print(ans)