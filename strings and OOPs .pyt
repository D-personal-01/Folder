class emp:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str): 
        for i in emp_str:
            if i.isalpha():
                continue
            else:
                 break
        return cls(emp_str.split(i)[0], int(emp_str.split(i)[1]), float(emp_str.split(i)[2]))

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

a=emp.from_string("John 30 50000")
b=emp.from_string("Alice-25-60000")
c=emp.from_string("Bob,40,70000")
a.display()
b.display()
c.display()
