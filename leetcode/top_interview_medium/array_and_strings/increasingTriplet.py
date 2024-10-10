def increasingTriplet(nums):
    if len(nums) < 3:
        return False
    x = y = MAX = 2**31
    for i in range(len(nums)):
        if nums[i] <= x:
            x = nums[i]
        elif nums[i] <= y:
            y = nums[i]
        else:
            return True
    return False


nums = [2,1,5,0,4,6]
nums = [3,4,2,5]
nums = [4,2,5]
nums = [3,4,2,5]
print(increasingTriplet(nums))