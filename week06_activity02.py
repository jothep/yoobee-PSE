data = ['a5', 'a2', 'b1', 'b3', 'c2']
sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
print(sorted_data)

'''
The lambda function sorts the data list. First, x[0] (i.e., 'a, b, c') is sorted, 
and then x[1] is sorted in int format, i.e., by numerical size. 
The final result is ['a2', 'a5', 'b1', 'b3', 'c2']
'''

students = [
    {'name': 'John', 'grade': 'A', 'age': 20},
    {'name': 'Jane', 'grade': 'B', 'age': 21},
    {'name': 'Joss', 'grade': 'A+', 'age': 19},
    {'name': 'Jack', 'grade': 'A-', 'age': 16},
    {'name': 'Dave', 'grade': 'C', 'age': 25},
]
# sorted by age
sorted_students_age = sorted(students, key=lambda x: x['age'])
print(sorted_students_age)

# sorted by grade
suffix_map = {'-': 0, '': 1, '+': 2}
sorted_students_grade = sorted(students, key=lambda x: (x['grade'][0], suffix_map.get(x['grade'][1:], 1)))
print(sorted_students_grade)


'''
Sorting dictionary students by "age"
Using function sorted, target is dictionary. 
Set dict as x, and sorted by age.

Sorting dictionary students by "grade"
Define a new dictionary called suffix_map which include symbles as key and set value for it.
Sort the first like x[0] of grade firstly in lambda,
Sort the second like x[1] of grade secondly in lambda.
'''

# Sort by age, then by salary if ages are the same
# use lambda
employees = [
    {'name': 'Alice', 'age': 30, 'salary': 80000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 120000},
    {'name': 'JSK', 'age': 30, 'salary': 70000} # add a line to test
]

sorted_employees = sorted(employees, key=lambda x: (x['age'], x['salary']))
print(sorted_employees)