
# Millorem l'eficiència amb un segment tree,
# per calcular eficientment els mínims

class ST():
    
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
    
    
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, m, k, d = line()
    res = []
    for i in range(n):
        v = line()
        cost = [1]
        for j in range(1, min(d+1, m)):
            cost.append(v[j] + 2)
        st = ST(cost)
        for j in range(d+1, m):
            minim = st.minim(1, d+1)
            cost.append(minim + v[j] + 1)
            st.change(j%(d+1), cost[-1])
        res.append(cost[-1])
    millor = sum(res[:k])
    cur = millor
    for i in range(n-k):
        cur += res[k+i]-res[i]
        millor = min(millor, cur)
    print(millor)