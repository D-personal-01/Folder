n=int(input("Enter the number of numbers you want to check: "))
a=int(input("Enter the number: "))
for i in range(n-1):
    b=int(input("Enter the number: "))
    if b>a:
        a=b
print(a)