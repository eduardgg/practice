
mod = int(1e9 + 7)
n = int(input())

if n & 1:
    print(0)

else:
    factorials = [1] * (n + 1)
    inverse_factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorials[i] = factorials[i - 1] * i % mod
    inverse_factorial[n] = pow(factorials[n], -1, mod)
    for i in range(n - 1, -1, -1):
        inverse_factorial[i] = inverse_factorial[i + 1] * (i + 1) % mod
    
    bin = factorials[n] * inverse_factorial[n//2] % mod * inverse_factorial[n//2] % mod
    catalan = bin * pow(n//2 + 1, -1, mod) % mod
    print(catalan)