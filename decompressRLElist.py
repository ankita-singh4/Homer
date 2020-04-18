def decompressRLElist(nums):
    output = []
    intermediate = []
    for i in range(0, len(nums)):
        intermediate.clear()
        if i % 2 == 0:
            freq = nums[i]
            value = nums[i+1]
            print(freq,value)
            intermediate = [value] * freq
            print(intermediate)
        output.extend(intermediate)
    return output


print(decompressRLElist([1,1,2,3]))