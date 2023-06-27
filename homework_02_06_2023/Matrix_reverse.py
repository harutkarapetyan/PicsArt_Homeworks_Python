def reverse(matrix):
    toxer = len(matrix)
    matrix = matrix[::-1]

    for i in range(toxer):
        matrix[i] = matrix[i][::-1]
    return matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

result = reverse(matrix)

for i in result:
    print(i)
