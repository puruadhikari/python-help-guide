nums = [1,2,3,4]
length = len(nums)
prefix = 1
prefix_array = [1] * length
suffix_array = [1] * length

for i in range(length):
    prefix_array[i] = prefix
    prefix = prefix * nums[i]

suffix = 1

for j in range(length - 1, -1, -1):
    suffix_array[j] = suffix
    suffix = suffix * nums[j]

result = []

for index in range(length):
    result.append(suffix_array[index] * prefix_array[index])

print(result)