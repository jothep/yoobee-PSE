# extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]
result = [person for person in data if person["age"] > 25]
print(result)

# use list comprehension to flatten the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list1 = [num for row in matrix for num in row]
print(list1)

matrix2 = [[0, 2, -3], [4, -5, 16], [17, 18, 39]]
# Sum_matrix = matrix + Matrix2 ...?
# Mul_matrix = matrix * Matrix2 ...?

# Sum matrix
addition_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        addition_result[i][j] = matrix[i][j] + matrix2[i][j]

print(addition_result)

# multiply matrix
multiplication_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(matrix)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            multiplication_result[i][j] += matrix[i][k] * matrix2[k][j]

print(multiplication_result)