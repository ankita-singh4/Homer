def mountainArray(A):
    n = len(A)
    i = 0
    while i < n and A[i] < A[i+1]:
            i += 1
    if i == 0 or i == n-1:
            return False
    while i+1 <n and A[i] > A[i+1]:
            i += 1
    return True


print(mountainArray([3,5,5]))