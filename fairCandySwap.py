def fairCandySwap(A, B):
    sumA = sum(A)
    sumB = sum(B)
    setB = set(B)
    for i in A:
        if i + (sumB - sumA) / 2 in setB:
            return [i, i + (sumB - sumA) / 2]


A = [1,2,5]
B = [2,4]
print(fairCandySwap(A, B))