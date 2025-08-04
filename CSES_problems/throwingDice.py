

# No és eficient perquè n pot ser molt gran (10^15)
# Convolution és O(n^2), que és inviable.
# Inclús usar FFT, amb O(nlogn) seria molt ineficient.
# Cal trobar una recurrència i resoldre matricialment, amb O(logn).

MOD = 10**9 + 7

def conv(p, q):
    res = [0]*(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            res[i+j] = (res[i+j] + p[i]*q[j]) % MOD
    return res

n = int(input())
p = [0, 1, 1, 1, 1, 1, 1]
res = [1, 1, 1, 1, 1, 1, 1]
for _ in range(n.bit_length()):
    p = conv(p, p)
    p[0] += 1
    res = conv(res, p)
    p[0] -= 1

print(res[n])