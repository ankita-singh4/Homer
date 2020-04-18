def transpose(A):
    r, c = len(A), len(A[0])
    res = [[None for x in range(c)] for y in range(r)]
    print(res)
    for i, row in enumerate(A):
        for j, val in enumerate(row):
            res[j][i] = val
    return res


print(transpose([[[1,2,3],[4,5,6]]]))
