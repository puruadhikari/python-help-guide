nums1 = [1,2,3]
nums2 = [2,4,6]

set1 = set(nums1)
set2 = set(nums2)

print([list(set1-set2),list(set2-set1)])