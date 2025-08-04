
mod = 10**9 + 7
factorials = []
inverse_factorial = []

def precompute_factorials(n, mod):
    global factorials, inverse_factorial
    factorials = [1] * (n + 1)
    inverse_factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorials[i] = factorials[i - 1] * i % mod
    inverse_factorial[n] = pow(factorials[n], -1, mod)
    for i in range(n - 1, -1, -1):
        inverse_factorial[i] = inverse_factorial[i + 1] * (i + 1) % mod

def binomial(n, k, mod):
    if k < 0 or k > n:
        return 0
    return factorials[n] * inverse_factorial[k] % mod * inverse_factorial[n - k] % mod


n, m = map(int, input().split())
precompute_factorials(m+n, mod)
print(binomial(m+n-1, m, mod))