def diagonalTraversal(mat):
    output = []
    rows = len(mat)
    cols = len(mat[0])
    intermediate = []
    for d in range(cols + rows - 1):
        intermediate.clear()
        c = 0
        r = 0
        if d < cols:
            r = 0
        else:
            r = d - cols + 1
        if d < cols:
            c = d
        else:
            c = cols - 1
        #r, c = 0 if d < cols else d - cols + 1, d if d < cols else rows - 1
        while r < rows and c > -1:
            intermediate.append(mat[r][c])
            r += 1
            c -= 1
        if d % 2 == 0:
            output.extend(intermediate[::-1])
        else:
            output.extend(intermediate)
    return output


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(diagonalTraversal(matrix))
