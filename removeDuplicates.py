def removeDuplicates(nums):
    i = 0
    if len(nums) == 0: return -1
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i+1


print(removeDuplicates([0,0,1,1,1,2,2,3,4]))
