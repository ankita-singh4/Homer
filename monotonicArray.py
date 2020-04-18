def isMonotonic(A):
    j = 1
    for i in range(0, len(A)):
        if (i <= j and A[i] <= A[j]):
            print(A[i], A[j])
            j +=1
    return True



A = [1,2,5,4]
print(isMonotonic(A))