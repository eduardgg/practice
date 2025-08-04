
MOD = 998244353
n,m = [int(t) for t in input().split()]
m//= 2
 
b = [0,1]
for i in range(1,m+1):
    b.append( b[-1]*(2*m+1-i)*pow(i,-1,MOD)%MOD )
c = [b[i+1]-b[i] for i in range(m+1)]

def mul(P,Q):
    R = []
    for i in range(m+1):
        s = 0
        for x in range(i+1):
            s += P[x]*Q[i-x]
        R.append( s%MOD )
    return R
 
p = [0]*(m+1); p[0] = 1
acc = c[::-1]
print(acc)
 
e = n-1
while e:
    if e&1: p = mul(p,acc)
    acc = mul(acc,acc)
    e >>= 1
 
print( mul(p,c)[m] )