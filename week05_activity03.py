class   User:
    def __init__(self, name, address, age):
        self.name   = name
        self.address = address
        self.age    = age

    def allow_to_enter(self):
        print("allow to enter campus")
#A subclass can directly inherit the attributes of its superclass.
        
class   students(User):
    def __init__(self, name, address, age,student_id ,record):
        super().__init__(name, address, age)
        self.student_id = student_id
        self.record = record

class   academics(User):
    def __init__(self, name, address, age, academic_id, tax_code, rate):
        super().__init__(name, address, age)
        self.academic_id = academic_id
        self.tax_code = tax_code
        self.rate = rate

class   General_staffs(User):
    def __init__(self, name, address, age, staff_id, tax_code, rate):
        super().__init__(name, address, age)
        self.staff_id = staff_id
        self.tax_code = tax_code
        self.rate = rate