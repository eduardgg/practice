
for _ in range(int(input())):
    n, l, r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    esq = a[:l-1]
    mig = a[l-1:r]
    top1 = sum(mig)
    esq.sort(reverse = True)
    mig.sort()
    while esq and mig and esq[-1] < mig[-1]:
        top1 -= (mig.pop() - esq.pop())

    dre = a[r:]
    mig = a[l-1:r]
    top2 = sum(mig)
    dre.sort(reverse = True)
    mig.sort()
    while dre and mig and dre[-1] < mig[-1]:
        top2 -= (mig.pop() - dre.pop())
    
    top = min(top1, top2)
    print(top)