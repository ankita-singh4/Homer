def sortArrayByParity2(A):
    j = 1
    for i in range(0, len(A), 2):
        if A[i] % 2:
            print(A[i])
            while A[j] % 2:
                j += 2
                print(j, A[j])
            A[i], A[j] = A[j], A[i]
    return A

print(sortArrayByParity2([1,3,2,5,4]))