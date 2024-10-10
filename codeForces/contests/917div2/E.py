
for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    if k % 2:
        ok = False

    elif not k % 4:
        ok = True
        M = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n//2):
            if not k: break
            for j in range(n//2):
                if not k: break
                M[2*i][2*j] = 1
                M[2*i+1][2*j] = 1
                M[2*i][2*j+1] = 1
                M[2*i+1][2*j+1] = 1
                k -= 4

    elif n == k == 2:
        ok = True
        M = [[0, 1], [1, 0]]

    elif 2 < k <= n*n//2:
        ok = True
        M = [[0 for _ in range(n)] for _ in range(n)]
        M[0][0] = M[0][1] = 1
        M[1][1] = M[1][2] = 1
        M[2][2] = M[2][0] = 1
        k -= 6
        i = 3
        for i in range(2, n//2):
            if not k: break
            for j in range(n//2):
                if not k: break
                M[2*i][2*j] = 1
                M[2*i+1][2*j] = 1
                M[2*i][2*j+1] = 1
                M[2*i+1][2*j+1] = 1
                k -= 4

    elif n*n - 2 > k >= n*n//2:
        ok = True
        M = [[1 for _ in range(n)] for _ in range(n)]
        M[0][0] = M[0][1] = 0
        M[1][1] = M[1][2] = 0
        M[2][2] = M[2][0] = 0
        k = n*n - k
        k -= 6
        i = 3
        for i in range(2, n//2):
            if not k: break
            for j in range(n//2):
                if not k: break
                M[2*i][2*j] = 0
                M[2*i+1][2*j] = 0
                M[2*i][2*j+1] = 0
                M[2*i+1][2*j+1] = 0
                k -= 4

    else:
        ok = False
    
    if ok:
        print("Yes")
        for v in M:
            print(*v)
            
    else:
        print("No")