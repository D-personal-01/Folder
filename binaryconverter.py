
while 1:
    num=int(input("Enter the number or 999 to exit: "))
    if num==999:
        print("exiting")
        exit(1)
    elif num<0:
        print ("Re-enter any diffrent non-negetive number.")
    else:
        while num!=0:
            print(num%2,end="")
            num//=2
    print()