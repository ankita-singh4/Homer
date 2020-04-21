def isMonotonic(A):
    s = 0
    for i in range(len(A)-1):
        comp = compare(A[i], A[i+1])
        print(compare)
        if compare:
            if compare != s != 0:
                return False
            s = compare
    return True


def compare(a,b):
    if a < b:
        return True
    else: return False

A = [6,5,4,4]
print(isMonotonic(A))