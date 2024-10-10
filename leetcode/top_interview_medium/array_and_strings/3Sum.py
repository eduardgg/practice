def threeSum(nums):
    nums.sort()
    n = len(nums)
    solution = []
    for i in range(n-2):
        x = nums[i]
        low = i+1
        high = n-1
        while low < high:
            y = nums[low]
            z = nums[high]
            if x + y + z == 0:
                if [x,y,z] not in solution:
                    solution.append([x,y,z])
                low = low + 1
                high = high - 1
            elif x + y + z > 0:
                high = high - 1
            else:
                low = low + 1
    return solution


print(threeSum([]))
print(threeSum([0]))
print(threeSum([0,1]))
print(threeSum([-1,0,1]))
print(threeSum([-1,0,1,2,-1,-4]))