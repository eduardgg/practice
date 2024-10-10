t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    esq = -1
    for i in range(len(s)):
        if s[i] == 'A':
            esq = i
            break
    if esq == -1:
        print(0)
        continue

    dre = -1
    j = len(s)-1
    while j >= esq:
        if s[j] == 'B':
            dre = j
            break
        j -= 1
    if dre == -1:
        print(0)
        continue
    
    print(dre-esq)