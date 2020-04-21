def heightChecker(heights):
    shortest = sorted(heights)
    print(shortest)
    count = 0
    for i in range(len(heights)):
        if shortest[i] != heights[i]:
            count += 1
    return count


heights = [1,1,4,2,1,3]
print(heightChecker(heights))
