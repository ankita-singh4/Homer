def two2sums(numbers, target):
    low = 0
    high = len(numbers) -1
    while low < high:
        sum = numbers[low] + numbers[high]
        if sum == target:
            return [low+1, high+1]
        elif sum < target:
            low += 1
        else:
            high -= 1
    return [-1, -1]


print(two2sums([2,7,11,15], 9))