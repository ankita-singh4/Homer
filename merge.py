def merge(nums1, m, nums2, n):
    c = nums1[:m]
    nums1[:] = []
    a = 0
    b = 0
    while a < m and b < n:
        if c[a] < nums2[b]:
            nums1.append(c[a])
            a += 1
        else:
            nums1.append(nums2[b])
            b += 1
    if a < m:
        nums1[a + b:] = c[a:]
    if b < n:
        nums1[a + b:] = nums2[b:]


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))