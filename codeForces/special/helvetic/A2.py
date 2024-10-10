
a = input()
n = len(a)

prefix = []
cur = -1
i = 0
o, t = 0, 0

while i < n:
    cur += 1
    obj = o
    o, t = 0, 0
    while i < n:
        if a[i] == '(':
            o += 1
        elif t == obj:
            break
        else:
            t += 1
        prefix.append(cur)
        i += 1

last = [0]*(prefix[-1]+1)
for i in range(n):
    last[prefix[i]] = i

ans = []
cur = 0
while len(ans) < n:
    pos = last[cur]
    last[cur] -= 1
    ans.append(a[pos])
    if a[pos] == '(':
        cur += 1
    else:
        cur -= 1

for e in ans:
    print(e, end="")