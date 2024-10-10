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

# Exemple d'ús
vector = [20, 1, 20, 6, 4, 5]
num_inversions = count_inversions(vector)
print(f"Nombre d'inversions: {num_inversions}")
print(f"Vector ordenat: {vector}")