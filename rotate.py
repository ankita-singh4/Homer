def rotate(nums, k):
    j = 0
    while(j < k):
        for i in range(0, len(nums)):
            temp = nums[i]
            nums[i] = nums[len(nums)-1]
            nums[len(nums)-1] = temp
        j+=1
    return nums


print(rotate([1,2,3,4,5], 4))
