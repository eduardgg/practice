
for _ in range(int(input())):
    l, r = 2, 1000
    while r-l > 1:
        m1 = l + (r-l)//3
        m2 = l + 2*(r-l)//3
        print("?", m1, m2, flush = True)
        ans = int(input())
        if ans == m1*m2:
            l = m2+1
        elif ans == m1*(m2+1):
            l = m1+1
            r = m2+1
        else: # ans == (m1+1)*(m2+1)
            r = m1+1
    print("!", l, flush = True)