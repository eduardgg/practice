
# Observacions clau:
# Perquè el XOR dels 1s, 2s, 3s i 4s sigui 0 cal:
#   1. Tants 1s com 3s (en mòdul 2), o sigui p1%2 = p3%2
#   2. Tants 2s com 3s (en mòdul 2), o sigui p2%2 = p3%2
#   3. Cap 4 (en mòdul 2), o sigui p4%2 = 0
# A partir d'aquí simplement els anem eliminant de manera
# greedy (per parelles), mantenint sempre que sigui possible
# una combinació guanyadora pel Bob (condicions amunt)

for _ in range(int(input())):
    p1, p2, p3, p4 = list(map(int, input().split()))
    ans = 0
    if p1%2 and p2%2 and p3%2:
        ans += 1
    ans = ans + p1//2 + p2//2 + p3//2 + p4//2
    print(ans)