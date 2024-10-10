def countSmaller(nums):
    sorted = [nums.pop()]
    smallers = [0]
    while len(nums) > 0:
        numero = nums.pop()
        low = 0
        high = len(sorted)
        while low < high:
            med = (low + high) // 2
            if sorted[med] < numero:
                low = med + 1
            else:
                high = med
        smallers.append(low)
        sorted.insert(low, numero)
    smallers.reverse()
    return smallers

nums = [5,2,6,1]
print(countSmaller(nums))

nums = [5,2,6,1,7,1,8,3]
print(countSmaller(nums))