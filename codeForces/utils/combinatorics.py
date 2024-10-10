
# Quan cal calcular diversos factorials, en valors controlats (ex: n = 10**6),
# pot sortir a compte guardar-los tots en un vector.
# De la mateixa manera, els inversos dels factorials (per calcular, per
# exemple, nombres combinatoris), que es poden trobar eficientment.

mod = 10**9 + 7

def init_fact(n):
    fact = [1]
    for i in range(n):
        fact.append((fact[-1]*(i+1)) % mod)
    invfact = [pow(fact[-1], -1, mod)]
    for i in range(n, 0, -1):
        invfact.append((invfact[-1]*i) % mod)
    invfact = invfact[::-1]
    return fact, invfact

fact, invfact = init_fact(2*(10**5))

# Llavors podem calcular el nombre n sobre k (en mòdul m), usant la funció:
def choose(n, k, m):
    if n < 0 or k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] * invfact[n-k]) % m

# Els nombres d'Stirling de primera espècie [n, k] poden ser bastant útils en
# alguns problemes de Combinatòria. Compten el nombre de permutacions que es
# poden fer amb n elements, amb exactament k cicles.

def init_stirling(n):
    stirling = [[0 for _ in range(n+1)] for _ in range(n+1)]
    stirling[1][1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            stirling[i][j] = stirling[i-1][j-1] + (i-1)*stirling[i-1][j]
    return stirling

stirling = init_stirling(2*(10**5))

# Python incorpora un mètode més senzill per calcular potències
# modulars, inclús d'exponents negatius (inversos modulars):
#       pow(base, exp, mod)

# Exponenciació modular eficient (per exponents >= 0)
def exp_modular(base, exponent, mod):
    result = 1
    # Convertim l'exponent a binari per utilitzar l'algorisme de l'exponenciació modular ràpida
    binary_exponent = bin(exponent)[2:]
    # Iterem sobre els bits de l'exponent, de dreta a esquerra
    for bit in binary_exponent[::-1]:
        if bit == '1':
            result = (result * base) % mod
        base = (base * base) % mod
    return result

def mod_inverse(x, m):
    """
    Retorna l'invers modular de x mòdul m.
    """
    _, result, _ = extended_gcd(x, m)
    return result % m

def extended_gcd(a, b):
    """
    Retorna els tres nombres g, x, y tals que:
    g = gcd(a, b), ax + by = g
    Si l'equació diofàntica és ax + by = kg, i trobem una solució (x0, y0), llavors
    una solució és (kx0, ky0), i la general (kx0-cb, ky0-ca), per tot c enter.
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def binomial_coefficient_mod(n, k, m):
    """
    Retorna el coeficient binomial (n sobre k) mòdul m.
    """
    if k < 0 or k > n:
        return 0

    result = 1

    for i in range(1, min(k, n - k) + 1):
        result = (result * (n - i + 1) % m) * mod_inverse(i, m) % m

    return result

def permutations_without_repetition_mod(n, k, m):
    """
    Retorna les permutacions de subconjunts sense repetició (n!/(n-k)! % m).
    """
    if k < 0 or k > n:
        return 0

    result = 1
    for i in range(n, n - k, -1):
        result = (result * i) % m

    return result

def factorial_mod(n, m):
    """
    Retorna el factorial de n (n! % m).
    """
    return permutations_without_repetition_mod(n, n, m)