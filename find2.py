def findNumber(num):

    for n in range(0, len(num)):
        if num[n] == 2:
            return True
    return False



num = [1, 3, 4]
print(findNumber(num))
