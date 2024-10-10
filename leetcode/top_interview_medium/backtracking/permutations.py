def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    answer = []
    for i in range(len(nums)):
        n = nums[i]
        for j in permute(nums[0:i] + nums[i+1:len(nums)]):
            if type(j) == int:
                j = [j]
            answer.append([n]+j)
    return answer

nums = [1,2,3,4]
print(permute(nums))
nums = [1]
print(permute(nums))
nums = [0,1]
print(permute(nums))