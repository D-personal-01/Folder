class employee:
    def __init__(self, name, age, salary, designation,dept):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation
        self.department = dept

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Designation: {self.designation}, Department: {self.department}")


class programmer(employee):
    def __init__(self, name, age, salary, designation, dept, programming_language):
        super().__init__(name, age, salary, designation, dept)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


emp1 = employee("John Doe", 30, 50000, "Manager", "Sales")
emp2 = programmer("Jane Smith", 28, 60000, "Software Engineer", "IT", "Python")
emp1.display_info()
emp2.display_info()