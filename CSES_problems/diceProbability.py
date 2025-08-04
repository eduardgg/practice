
def conv(p, q):
    res = [0]*(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            res[i+j] += p[i]*q[j]
    return res

def pow(p, n):
    res = [1]
    while n:
        if n&1:
            res = conv(res, p)
        p = conv(p, p)
        n >>= 1
    return res

n, a, b = map(int, input().split())
a = max(a, 1*n)
b = min(b, 6*n)
p = [1/6]*6
q = pow(p, n)
ans = sum(q[a-n:b+1-n])
print(format(ans, ".6f"))