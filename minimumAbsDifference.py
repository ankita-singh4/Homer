def minAbsDifference(arr):
    arr.sort()
    minSum = float('inf')
    res = []
    for i in range(len(arr) -1):
        if abs(arr[i]-arr[i+1]) < minSum:
            minSum = abs(arr[i] - arr[i+1])

    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) == minSum:
            res.append([arr[i], arr[i+1]])
    return res


print(minAbsDifference([3,8,-10,23,19,-4,-14,27]))
