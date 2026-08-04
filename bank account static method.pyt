class bankaccount:
    Bank_balance=0
    pin=None
    # Static method is used to access the class variables without creating an instance of the class.
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
a.set_pin(000)
a.set_pin(192837)

a.initial_bb(99999999999.99)
