def pascalsTriangle(numrows):
    triangle = []
    for rows in range(numrows):
        r = [None for _ in range(rows+1)]
        r[0], r[-1] = 1, 1
        for i in range(1, len(r) -1):
            r[i] = triangle[rows -1][i-1] + triangle[rows - 1][i]
        triangle.append(r)
    return triangle


print(pascalsTriangle(6))
