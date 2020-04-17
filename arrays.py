def pivotIndex(num):
    sum_l = 0
    sum_r = sum(num)
    for i in range(0, len(num)):
        if sum_l == (sum_r - sum_l - num[i]):
            return i
        print(sum_l, sum_r)
        sum_l += num[i]
    return -1


num = [1, 7, 3, 6, 5, 6]
j = pivotIndex(num)
print(j)
# print(numbers[1:4])
# maximum = numbers[0]
# for num in numbers:
#     if num > maximum:
#         maximum = num
#
# print(maximum)
