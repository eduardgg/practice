
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    a, b, c = line()

    # La c només serveix per encaixar
    if a+1 != c:
        print(-1)
        continue

    # Prioritzem posar els 'a' tan amunt possible
    h = a.bit_length()
    lliures = 2**h-1-a
    b -= lliures
    if b > 0:
        h += (b-1)//(a+1)+1
    
    print(h)