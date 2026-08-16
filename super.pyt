class parent:

    def __init__(self):
        print("parent class constructor")

    def show(self):
        print("parent class method")

class child(parent):
    
    def __init__(self):
        super().__init__()
        print("child class constructor")

    def show(self):
        super().show()
        print("child class method")


obj = child()
obj.show()