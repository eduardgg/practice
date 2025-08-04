
from collections import Counter

c = Counter(input())
chars = list(c.keys())
chars.sort()
v = []
res = []
def f():
    if not any(c.values()):
        res.append(''.join(v))
    for cha in chars:
        if c[cha]:
            c[cha] -= 1
            v.append(cha)
            f()
            v.pop()
            c[cha] += 1
f()
print(len(res))
for s in res:
    print(s)