class bankaccount:
    Bank_balance=0
    pin=None
    # Static method is used to access the class variables without creating an instance of the class.
    def __init__(self):
        a=int(input("Enter your bank balance: "))
        b=int(input("Enter your pin: "))
        self.set_pin(b)
        self.initial_bb(a)
    @staticmethod
    def set_pin(new_pin):
        if len(str(new_pin))==6:
            pin=new_pin
            print("Pin set successfully")
        else:
            print("Pin must be 6 digits long")
    @staticmethod
    def initial_bb(bb):
        if bb>=30000:
            Bank_balance=bb
            print("Bank balance set successfully")
        else:
            print("Initial bank balance cannot be less than 30000")

a=bankaccount()

