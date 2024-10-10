
for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = 1
    st = set()
    for e in a:
        if x%e == 0 and x//e in st:
            st = {e}
            ans += 1
        else:
            l = list(st)
            for i in l:
                if i*e <= x//2:
                    st.add(i*e)
            st.add(e)
    print(ans)