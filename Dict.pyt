class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p=person("Alice", 30)
print(p.__dict__)