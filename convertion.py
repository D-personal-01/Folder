
while 1:
    print()
    c=int(input("Enter \n1 to convert grams to kilograms \n2 to convert meters to kilo meters \n3 to exit \n-->"))
    
    if c==1:
        g=int(input("Enter grams: "))
        print(f"{g}g is {g/1000}kg")
    elif c==2:
        m=int(input("Enter meters: "))
        print(f"{m}m is {m/1000}km")
    elif c==3:
        exit(1)
        
    else:
        print("invalid choice")
