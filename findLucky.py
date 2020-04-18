def findLucky(arr):
    d = {x: arr.count(x) for x in arr}
    output = []
    for key, value in d.items():
        if key == value:
            output.append(key)
            # print(output)
    if len(output) > 0:
        return max(output)
    else:
        return -1





print(findLucky([7,7,7,7,7,7,7]))
