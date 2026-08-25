class citizen:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class student(citizen):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")

class candidate(student):
    def __init__(self, name, age, student_id, election_id):
        super().__init__(name, age, student_id)
        self.election_id = election_id

    def display(self):
        super().display()
        print(f"Registration ID: {self.student_id}")


print(candidate.mro())