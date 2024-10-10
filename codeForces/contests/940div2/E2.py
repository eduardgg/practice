 
m = 10**6
p = [0,0]+[1]*(m-1)
q = [[] for _ in range(m+1)]
for i in range(2,m+1):
    if p[i]:
        q[i] += i,
        for j in range(2*i,m+1,i):
            p[j] = 0
            q[j] += i,

print(q[:20])

r = [0]*(m+1)
d = {i:0 for i in range(m+1) if p[i]}
c = 0
for i in range(2,m+1):
    for p in q[i]:
        if p>2:
            if not d[p]:
                d[p] = p-1
                c += p-1
            else:
                d[p] -= 1
                c -= 1
        elif i&7:
            d[p] += 1
            c += 1
        else:
            d[p] -= 3
            c -= 3
    r[i] = (r[i-1]+c) % (10**9+7)

for _ in range(int(input())):
    print(r[int(input())])