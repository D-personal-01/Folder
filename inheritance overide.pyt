class citizen:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def social_status(self):
        return "Citizen"

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class granted_citizenship(citizen):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

    def social_status(self):
        return "Granted Citizenship"

    def display(self):
        super().display()
        print(f"Country: {self.country}")

A = citizen("Alice", 30)
B = granted_citizenship("Bob", 25, "USA")
A.display() 
B.display() 