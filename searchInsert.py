def searchInsert(nums, target):
    # solve using binary search
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return left


print(searchInsert([1,3,5,7,9], 0))
