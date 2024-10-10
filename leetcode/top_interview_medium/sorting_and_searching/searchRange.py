
def searchRange(nums, target):
    # nums is a sorted array

    if len(nums) == 0 or nums[0] > target or nums[-1] < target:
        return [-1,-1]

    # Trobem l'inici del rang:
    if nums[0] == target:
        inici = 0
    else:
        low = 0
        high = len(nums) - 1
        while high - low > 1:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid
            else:
                high = mid
        if nums[high] != target:
            return [-1,-1]
        inici = high

    # Trobem el final del rang:
    if nums[-1] == target:
        final = len(nums) - 1
    else:        
        low = inici
        high = len(nums) - 1
        while high - low > 1:
            mid = (low + high) // 2
            if nums[mid] == target:
                low = mid
            else:
                high = mid
        final = low

    # Retornem el rang
    return [inici, final]


print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([],0))
print(searchRange([3],3))
print(searchRange([3],5))
print(searchRange([1,2],0))
print(searchRange([1,2],1))
print(searchRange([1,2],2))
print(searchRange([1,2],3))
print(searchRange([2,2],0))
print(searchRange([2,2],2))
print(searchRange([1,2,3],1))