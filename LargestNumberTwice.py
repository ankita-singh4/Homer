def dominantIndex(nums):
    maximum = max(nums)
    index = nums.index(maximum)
    # nums.remove(maximum)
    for i in range(0, len(nums)):
        if nums[i] > (maximum/2) and nums[i] != maximum:
            return -1
    return index


numbers = [3, 6, 1, 0]
print(dominantIndex(numbers))

