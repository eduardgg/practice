def canJump(nums):
    aux = 0
    if nums[aux] == 0:
        if len(nums) == 1:
            return True
        return False
    maxim = nums[aux]
    while maxim < len(nums)-1:
        aux, maxim = maxim, max(i+nums[i] for i in range(aux+1,maxim+1))
        if aux == maxim:
            return False
    return True
            
nums1 = [2,3,1,1,4]
print(canJump(nums1))

nums2 = [3,2,1,0,4]
print(canJump(nums2))

nums3 = [0,1]
print(canJump(nums3))

nums4 = [0]
print(canJump(nums4))