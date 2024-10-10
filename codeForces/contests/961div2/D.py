
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

    dp = {e for e in range(1 << c) if e & (1 << (ord(s[-1]) - ord('A')))}
    for ss in substrs:
        for sdp in list(dp):
            if not (ss & sdp):
                dp.remove(sdp)

    ans = min([st.bit_count() for st in dp])
    print(ans)