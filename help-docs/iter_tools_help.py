from itertools import permutations, combinations
from itertools import product
data = [1,2,3]
data1 = ['a','b']
#permutation with length of the data
perm = permutations(data)
#permutation with length of 2
perm_2 = permutations(data,2)

print("permutations are: " , list(perm))
print("permutations are two items are: ", list(perm_2))

comb = combinations(data, len(data))
comb_2 = combinations(data,2)
print("combinations are: " , list(comb))
print("combinations are two items are: ", list(comb_2))

#this is Cartesian product of input iterables
result = list(product(data,data1))
print(result)


