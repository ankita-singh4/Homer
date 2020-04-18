def missingNumbers(nums):
    n = len(nums)
    sumE = (len(nums) * (len(nums) + 1)) // 2
    sumA = sum(nums)
    return sumE - sumA


print(missingNumbers([0, 1, 3]))
