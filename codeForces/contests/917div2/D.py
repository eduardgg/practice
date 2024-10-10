

# Counting inversions:

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Índex inicial del subvector de l'esquerra
    j = mid + 1 # Índex inicial del subvector de la dreta
    k = left    # Índex inicial del subvector temporani
    inv_count = 0

    # Unir les dues meitats mentre comptem les inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Copiar els elements restants de l'esquerra, si n'hi ha
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copiar els elements restants de la dreta, si n'hi ha
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copiar el subvector ordenat al vector original
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def count_inversions(arr):
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)



# Fenwick Tree:

def fw_create(t):
    for i in range(len(t)):
        c = t[i]
        i = i | i+1
        if i < len(t):
            t[i] += c
    return t

def fw_query(t, i):
    s = 0
    i = min(i, len(t))
    while i:
        s += t[i-1]
        i = i & i-1
    return s

def fw_update(t, i, c):
    while i < len(t):
        t[i] += c
        i = i | i+1




mod = 998244353
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    p = line()
    q = line()

    invs = 0
    t = [0]*(2*n)
    fw = fw_create(t)
    for e in p:
        ee = e
        j = 1
        while ee > 0 and j <= k:
            qua = (k-j)*(k-j+1)//2
            nous = fw_query(t, ee+1) - fw_query(t, ee//2+1)
            invs = (invs + nous*qua) % mod
            # print("debug", invs, "ee", ee, "nous", nous, "qua", qua)
            ee //= 2
            j += 1
        ee = e
        j = 1
        while ee <= 2*n and j <= k:
            qua = k*k - (k-j)*(k-j+1)//2
            nous = fw_query(t, ee*2+1) - fw_query(t, ee+1)
            invs = (invs + nous*qua) % mod
            # print("debug", invs, "ee", ee, "nous", nous, "qua", qua)
            ee *= 2
            j += 1
        # print(t)
        fw_update(fw, e, 1)

    invs += count_inversions(q)*n
    invs %= mod
    print(invs)