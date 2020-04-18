def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print(nums[i]+nums[j], i, j)
                #print(nums.index(nums[i]), nums.index(nums[j]))
                return [i, j]
    return -1


print(twoSum([2,7,11,15], 9))
