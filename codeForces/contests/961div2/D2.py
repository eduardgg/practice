
for _ in range(int(input())):
    n, c, k = list(map(int, input().split()))
    s = input()
    
    bm = 0
    prefix = [0]*26
    for i in range(k):
        pos = ord(s[i]) - ord('A')
        prefix[pos] += 1
        bm |= (1 << pos)
    
    substrs = {bm}
    for i in range(n-k):
        newpos = ord(s[k+i]) - ord('A')
        oldpos = ord(s[i]) - ord('A') 
        prefix[newpos] += 1
        prefix[oldpos] -= 1
        bm |= (1 << newpos)
        if prefix[oldpos] == 0:
            bm -= (1 << oldpos)
        substrs.add(bm)
    substrs.add(1 << ord(s[-1]) - ord('A'))
    
    bad = [False]*(1 << c)
    for ss in substrs:
        bad[((1 << c) - 1) ^ ss] = True
    
    for i in range((1 << c) - 1, -1, -1):
        bad[i] |= any(bad[i | (1 << m)] for m in range(c))

    ans = min([st.bit_count() for st in range(1 << c) if not bad[st]])
    print(ans)