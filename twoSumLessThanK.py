def twoSumLessThanK(A, K):
        A.sort()
        i, j, s = 0, len(A) - 1, -1
        while i < j:
            if A[i] + A[j] < K:
                s = max(s, A[i] + A[j])
                print(A[i], A[j])
                i += 1
            else:
                j -= 1
        return s


    # A.sort()
    # i, j, res = 0, len(A) - 1, -1
    #
    # while i < j:
    #     if A[i] + A[j] < K:
    #         res = max(res, A[i] + A[j])
    #         i += 1
    #     else:
    #         j -= 1
    #
    # return res

A = [10,20, 30]
K = 15
print(twoSumLessThanK(A,K))