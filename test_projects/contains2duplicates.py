def contains2duplicate(nums, k):
    j = 1
    for i in range(0, len(nums)):
        if nums[i] == nums[j]:
            if abs(i-j) == k:
                return [i, j]
        else:
            print(j)
            j += 1
    return -1


print(contains2duplicate([1, 2, 3, 1], 3))
