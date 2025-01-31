"""
given a matrix transpose it

input : matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Output:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""
matrix = [
    [1, 2, 3,1],
    [4, 5, 6,1],
    [7, 8, 9,1]
]
trans = zip(*matrix)
for rows in trans:
    print(rows)

transposed_matrix = []
for i in range(len(matrix[0])):
    col = []
    for j in range(len(matrix)):
        #NOTE : it is J and the I
        col.append(matrix[j][i])
    transposed_matrix.append(col)

print(transposed_matrix)