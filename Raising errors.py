inp=input("Enter a number or write quit to exit: ")
if inp.lower()=="quit":
    print(f"you wrote {inp} exiting the program")
else:
    try:
        inp=int(inp)
        if inp>=1 and inp<=1000:
            print(f"You entered the number {inp}")
            for i in range(1,inp+1):
                print("Lets make this world a better place!")
        else:
            raise ValueError("The number is out of range")
    except ValueError as ve:
        print("Error:",ve)
