def removeElements(nums, val):
    i = 0
    if len(nums) == 0: return -1
    for j in range(0, len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


print(removeElements([0,1,2,2,3,0,4,2], 2))