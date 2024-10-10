t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    minJ = min(a)
    maxJ = max(a)
    minG = min(b)
    maxG = max(b)
    sumJ = sum(a)
    sumG = sum(b)
    sumJ += max(0, maxG - minJ)
    if k%2 == 1:
        print(sumJ)
    else:
        dif = max(maxJ, maxG) - min(minJ, minG)
        sumJ -= dif
        print(sumJ)