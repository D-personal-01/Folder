class parent:

    def __init__(self):
        print("parent class constructor")
    



class child(parent):
    
    def __init__(self):
        super().__init__()
        print("child class constructor")




obj = child()
