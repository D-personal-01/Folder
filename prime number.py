a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
for n in range (a,b+1):
    f=1
    for i in range(2,(n//2)+1):
        if n%i==0:
            f=0
            print(n,"Not prime")
            break

    if f:
        print(n,"Prime")
