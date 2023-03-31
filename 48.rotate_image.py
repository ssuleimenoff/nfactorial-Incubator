def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(rotate(matrix))
