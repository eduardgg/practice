
def solve(k):
    dec = [False]*n
    acum = 0
    for i in range(n-k):
        acum ^= dec[i]
        if not (int(s[i]) ^ acum):
            acum ^= 1
            dec[i+k] = True
        
    acum ^= dec[n-k]
    e = int(s[n-k]) ^ acum
    ok = True
    for i in range(n-k+1, n):
        acum ^= dec[i]
        if (int(s[i]) ^ acum) != e:
            ok = False
            break

    return ok



for _ in range(int(input())):
    n = int(input())
    s = input()

    fet = True
    zeros = s.count('0')
    for i in range(n-1):
        if s[0] != s[i+1]:
            fet = False
            break
    if fet:
        print(n)
        continue

    k = n
    while k:
        # Lineal, evitant binary search...
        # Tot i que potser es podria arreglar!
        if solve(k):
            print(k)
            break
        k -= 1


"""
    # Solució amb binary search
    # Vigilar cas: k%2 == 0 and zeros%2 != 0
    # No és possible però podria funcionar una k major
    l, r = 1, n
    while r-l > 1:
        k = (r+l)//2
        if solve(k):
            l = k
        else:
            r = k
        
    print(l)
"""