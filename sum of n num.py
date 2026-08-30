n=int(input("Enter how many numbers to add: "))
sum=0
for i in range(n):
    a=int(input("Enter the number: "))
    sum=sum+a
print("sum: ",sum)
print("avg:",sum/n)