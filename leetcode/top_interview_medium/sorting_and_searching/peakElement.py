def findPeakElement(nums):
    # Consecutive numbers are guaranteed to be different
    
    if len(nums) <= 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums)-1

    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] > nums[i+2]:
            return i+1

nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))