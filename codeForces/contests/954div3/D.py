
t = int(input())
for tc in range(t):
    n = int(input())
    a = input()
    if n == 2:
        ans = int(a)
    elif n == 3:
        ans = min(int(a[0])*int(a[1:]), int(a[:2])*int(a[2]), int(a[0])+int(a[1:]), int(a[:2])+int(a[2]))
    else:
        if any(a[i] == '0' for i in range(n)):
            ans = 0
        else:
            ans = sum([int(e) for e in a])
            dig2 = min(int(a[i:i+2]) for i in range(n-1))
            if dig2%10 == 1:
                for j in range(1, 9):
                    if dig2+j in [int(a[i:i+2]) for i in range(n-1)]:
                        dig2 += j
                        break
            ans += dig2 - dig2%10 - dig2//10
            uns = sum([1 for e in a if e == '1'])
            ans -= uns
            if dig2%10 == 1: ans += 1
            if dig2//10 == 1: ans += 1
    print(ans)