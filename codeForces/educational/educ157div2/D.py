
# Si n fos sempre senar, seria facilíssim.
# N'hi hauria prou amb calcular l'xor a_0 + a_2 + a_4...,
# que hauria de ser equivalent a l'xor de tots els b_i (o sigui,
# de 0 a n-1) excepte l'últim, fet que permetria trobar aquest
# últim b_n-1, i a partir d'aquí els altres: b_i = b_(i+1) + a_i

# No sempre és així. Per tant, comencem inventant un b_0 i
# calculem els altres b_i fent b_(i+1) = b_i + a_i.
# Els nombres obtinguts no seran els finals, segurament, però
# només diferiran per un nombre, el qual s'ha de fer xor a tots.
# Per tant, si 2 b's es repeteixen, no hi hauria solució, cosa
# que està garantida, però també poden haver-hi nombres majors a n.
# En 0,...,n-1 sabem quants bits de cada hi ha d'haver, així que
# ho comparem amb els elements de b trobats i anem construint
# aquest element final (auxiliar) que xoregerem.

n = int(input())
a = list(map(int, input().split()))

p = [0]*20
b = [0]
for i in range(n-1):
    e = b[-1]^a[i]
    pos = 0
    while e >= (1<<pos):
        if e & (1<<pos):
            p[pos] += 1
        pos += 1
    b.append(e)

aux = 0
for i in range((n-1).bit_length()):
    num = n//((2**(i+1)))*(2**i) + max(n%((2**(i+1))) - (2**i), 0)
    if num != p[i]:
        assert(p[i] == n - num)
        aux += (1 << i)

for i in range(n):
    b[i] ^= aux

print(*b)