class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

print(help(person))

p=person("Alice", 30)
print(help(p))