
mod = int(1e9 + 7)
n = int(input())
s = input()

k = 0
for e in s:
    if e == '(':
        k += 1
    else:
        k -= 1
        if k < 0:
            break

if n & 1 or k < 0 or k > n-len(s):
    print(0)
else:
    factorials = [1] * (n + 1)
    inverse_factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorials[i] = factorials[i - 1] * i % mod
    inverse_factorial[n] = pow(factorials[n], -1, mod)
    for i in range(n - 1, -1, -1):
        inverse_factorial[i] = inverse_factorial[i + 1] * (i + 1) % mod
    n -= len(s)
    bin = factorials[n] * inverse_factorial[(n+k)//2] % mod * inverse_factorial[(n-k)//2] % mod
    catalanExtended = bin * (k+1) % mod * pow((n+k)//2+1, -1, mod) % mod
    print(catalanExtended)