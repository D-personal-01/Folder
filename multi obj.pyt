
class Emp:
    def __init__(self,name,age,salary,designation):
        self.name=name
        self.age=age
        self.salary=salary
        self.designation=designation

n=int (input ("Enter the number of employees:"))

for i in range(n):
    name=input(f"Enter employee {i+1} name: ")
    age=int(input(f"Enter employee {i+1} age: "))
    salary=float(input(f"Enter employee {i+1} salary: "))
    designation=input(f"Enter employee {i+1} designation: ")
    
    globals()[f"emp{i}"] = Emp(name, age, salary, designation)