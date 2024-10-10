nums = [2,3,-2,4]
nums = [-2,0,-1]
nums = [-3,-1,-1]
nums = [-2,3,-4]

maxims = [nums[0]]
prod = nums[0]
if nums[0] == 0:
    prod = 1
i = 1
if nums[0] < 0:
    trobat = True
    prod1 = nums[0]
else:
    trobat = False

while i < len(nums):
    prod = prod * nums[i]
    if nums[i] == 0:
        maxims.append(0)
        prod = 1
        trobat = False
    elif nums[i] < 0:
        if not trobat:
            trobat = True
            prod1 = prod
            maxims.append(nums[i])
        elif prod > 0:
            maxims.append(prod)
        else:
            maxims.append(prod // prod1)
    else:
        if maxims[i-1] <= 0:
            maxims.append(nums[i])
        else:
            maxims.append(maxims[-1] * nums[i])
    i += 1

print(nums)
print(maxims)