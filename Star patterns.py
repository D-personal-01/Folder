n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()

print("------------------------------------")


for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1 or i==0 or i==n-1)and not(i==j):
            print("*",end=" ")
        elif i==j or i==j==n-1:
            print("$",end=" ")     
        else:
            print(" ",end=" ")

    print()

print("------------------------------------")

for i in range(n):
    for j in range(n):
        
        if i==j or i==j==n-1:
            print("$",end=" ")
        elif i + j == n - 1:
            print("$",end=" ")
        elif (j==0 or j==n-1 or i==0 or i==n-1)and not(i==j):
            print("*",end=" ")  
        else:
            print(" ",end=" ")

    print()