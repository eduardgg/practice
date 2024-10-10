
class minST():
    
    def __init__(self, v):
        self.v = v
        self.len = 2**(len(v)-1).bit_length()
        l = self.len
        inf = float('inf')
        self.tree = [inf]*l + v + [inf]*(l-len(v))
        
        while l > 1:
            for i in range(l, 2*l):
                self.tree[i//2] = min(self.tree[i//2], self.tree[i])
            l //= 2
    
    def change(self, k, x):
        k += self.len
        self.tree[k] = x        
        while k > 1:
            k //= 2
            self.tree[k] = min(self.tree[2*k], self.tree[2*k+1])

    def minim(self, a, b):
        a += self.len - 1
        b += self.len - 1
        s = float('inf')
        while a <= b:
            if a%2 == 1:
                s = min(s, self.tree[a])
                a += 1
            if b%2 == 0:
                s = min(s, self.tree[b])
                b -= 1
            a //= 2
            b //= 2
        return s

class maxST():
    
    def __init__(self, v):
        self.v = v
        self.len = 2**(len(v)-1).bit_length()
        l = self.len
        inf = float('-inf')
        self.tree = [inf]*l + v + [inf]*(l-len(v))
        
        while l > 1:
            for i in range(l, 2*l):
                self.tree[i//2] = max(self.tree[i//2], self.tree[i])
            l //= 2
    
    def change(self, k, x):
        k += self.len
        self.tree[k] = x
        while k > 1:
            k //= 2
            self.tree[k] = max(self.tree[2*k], self.tree[2*k+1])

    def maxim(self, a, b):
        a += self.len - 1
        b += self.len - 1
        s = float('-inf')
        while a <= b:
            if a%2 == 1:
                s = max(s, self.tree[a])
                a += 1
            if b%2 == 0:
                s = max(s, self.tree[b])
                b -= 1
            a //= 2
            b //= 2
        return s
    

import bisect
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    a = line()
    b = line()

    sta = maxST(a)
    stb = minST(b)
    va = [[] for _ in range(n+1)]
    vb = [[] for _ in range(n+1)]

    ok = True
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
        va[a[i]].append(i)
        vb[b[i]].append(i)

    if not ok:
        print("NO")
        continue

    for z in range(len(vb)-1,-1,-1):
        for i in vb[z]:
            if a[i] == b[i]:
                continue
            
            esq, dre = False, False
            j = bisect.bisect_left(va[z], i)

            if j < len(va[z]):
                minb = stb.minim(i+1, va[z][j]+1)
                maxa = sta.maxim(i+1, va[z][j]+1)
                if minb == b[i] and maxa == b[i]:
                    dre = True

            if j > 0 and not dre:
                minb = stb.minim(va[z][j-1]+1, i+1)
                maxa = sta.maxim(va[z][j-1]+1, i+1)
                if minb == b[i] and maxa == b[i]:
                    esq = True

            ok = esq or dre
            if not ok:
                break
        if not ok:
            break

    if ok:
        print("YES")
    else:
        print("NO")