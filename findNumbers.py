def findNumbers(nums):
    count = 0
    for i in range(0, len(nums)):
        digit_count = 0
        while nums[i] > 0:
            nums[i] = nums[i] // 10
            digit_count += 1
        if digit_count % 2 == 0:
            count += 1
    return count


print(findNumbers([555,901,482,1771]))
