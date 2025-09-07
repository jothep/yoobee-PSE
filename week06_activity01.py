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

# Part2
# 1. use enumerate() for looping to add 5 extra point to each grade in the list, the 5th one add 10 
grades = [88, 92, 78, 65, 50, 94]

for index, grade in enumerate(grades):
  if index == 4:  # The 5th element is at index 4
    grades[index] = grade + 10
  else:
    grades[index] = grade + 5

print(grades)

# 2. filter out elements depend on their index:
# use list comprehension and enumerate() to get elements with even index
data = [100, 200, 300, 400, 500]

even_index_elements = [value for index, value in enumerate(data) if index % 2 == 0]
print(even_index_elements)

# 3. create a dictionary from lists using zip()
keys = ['name', 'age', 'grade']
values = ['Alice', 25, 'A']

my_dict = dict(zip(keys, values))
print(my_dict)