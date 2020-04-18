def smallerNumbersThanCurrent(nums):
    output = []
    for i in range(0, len(nums)):
        count = 0
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
        for k in range(0, i):
            if nums[i] > nums[k]:
                count += 1
        output.append(count)
        #print(output)
    return output


print(smallerNumbersThanCurrent([6,5,4,8]))