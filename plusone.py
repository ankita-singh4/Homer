def plusone(nums: object):
    n = len(nums)
    for i in reversed(range(n)):
        if nums[i] < 9:
            nums[i] += 1
            return nums
        nums[i] = 0
    if nums[0] == 0:
        nums.insert(0,1)
        return nums


print(plusone([9, 8, 9]))

