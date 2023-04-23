def merge(nums1, m, nums2, n):
    ptr1 = m - 1
    ptr2 = n - 1
    while ptr1 >= 0 and ptr2 >= 0:
        if nums1[ptr1] >= nums2[ptr2]:
            nums1[ptr1 + ptr2 + 1] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[ptr1 + ptr2 + 1] = nums2[ptr2]
            ptr2 -= 1
    # all the numbers in nums1 are moved to the end
    while ptr2 >= 0:
        nums1[ptr2] = nums2[ptr2]
        ptr2 -= 1
    # if all the numbers in nums1 are moved to the end, numbers in nums1 are in right place
