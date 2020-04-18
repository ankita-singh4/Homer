def containsDuplicates(nums):
    d = {x:nums.count(nums) for x in nums}
    if len(d) == 0: return False
    else:

        for k, v in d.items():
            print(k,v)
            if v > 0:
                return True
            elif v <= 0:
                return False


print(containsDuplicates([0,1,1,2]))