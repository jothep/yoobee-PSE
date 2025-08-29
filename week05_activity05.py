class   User:
    def __init__(self, name, address, age):
        self.name   = name
        self.address = address
        self.age    = age

    def print_info(self):
        print("This method from class User.")
#A subclass can directly inherit the attributes of its superclass.
        
class   Students(User):
    def __init__(self, name, address, age,student_id ,record):
        super().__init__(name, address, age)
        self.student_id = student_id
        self.record = record

    def print_info(self):
        print("This method from class Students.")

if __name__ == "__main__":
    u = User("User1", "Auckland", 33)
    s = Students("Student2", "Sidny", 44, "S001", "Good")

    print(s.name, s.address, s.age, s.student_id, s.record)

    u.print_info()
    s.print_info()