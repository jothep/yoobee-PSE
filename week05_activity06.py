class Student:
    def __init__(self, name, age):
        self.name = name # public​
        self._age = age # protected​
        self.__grade = 'A' # private​

    def get_grade(self):
        return self.__grade
    
    def great_score(self):
        if self.__grade == 'A':
            return 'Excellent Score'
        return  'Passed'

class newStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def show_info(self):
        print(f"name: {self.name}, age: {self._age}")

s = Student('Ali', 20)
print(s.name) # accessible​
print(s._age) # discouraged​
print(s.get_grade()) # correct way
print(s.great_score())

ns = newStudent('Bob', 22)
ns.show_info()
print(ns.get_grade())
print(ns.great_score())

#Encapsulation is the programming principle of bundling data (attributes) 
# and the methods that operate on that data within a single unit (like a class).