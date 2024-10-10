def kLargest(nums, k):

    # Solució curta:
    nums.sort()
    return nums[len(nums)-k]

    # Solució llarga:
    # (i sembla que menys eficient)
    """
    pivot = nums[0]
    smaller = []
    larger = []
    for n in nums[1:]:
        if n < pivot:
            smaller.append(n)
        else:
            larger.append(n)
    l = len(larger)
    if l >= k:
        return kLargest(larger, k)
    elif l == k-1:
        return pivot
    return kLargest(smaller, k-l-1)
    """


nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(kLargest(nums, k))