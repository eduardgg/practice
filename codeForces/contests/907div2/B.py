t = int(input())
for _ in range(t):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    
    sumes = [0]*31
    minim = 31
    for i in range(len(x)):
        if x[i] < minim:
            for j in range(x[i], 31):
                sumes[j] += 2**(x[i]-1)
            minim = x[i]
    
    for i in range(len(a)):
        facts = 0
        k = a[i]
        while k%2 == 0:
            facts += 1
            k //= 2
        a[i] += sumes[facts]
    
    for e in a:
        print(e, end = " ")
    print()
