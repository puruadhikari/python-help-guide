import heapq

nums = [6, 7, 9, 4, 3, 5, 8, 10, 1]

heapq.heapify(nums)

print(nums) # prints - [1, 3, 5, 4, 6, 9, 8, 10, 7]

# find kth largest elements
val = heapq.nlargest(2,nums)
print(val) # prints - [10,9]

val_s = heapq.nsmallest(2, nums)
print(val_s) # prints - [1,3]