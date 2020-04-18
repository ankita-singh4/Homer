def majorityElement(nums):
    n = len(nums)
    d = {x:nums.count(x) for x in nums}
    print(d)
    for key, value in d.items():
        print(n/2)
        if value >= n/2:
            return key
    return -1


print(majorityElement([3,2,3]))