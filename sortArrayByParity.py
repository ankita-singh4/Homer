def sortArrayByParity(A):
    return [x for x in A if x%2 == 0] + [x for x in A if x%2 == 1]


print(sortArrayByParity([1,2,3,4]))