def createTargetArray(nums, index):
    target = []
    for i in range(0, len(nums)):
        print(index[i], nums[i])
        target.insert(index[i], nums[i])
    return target


print(createTargetArray([1], [0]))