n=5
for i in range (1,n+1):
    print("*"*i)
for i in range (n-1,0,-1):
    print("*"*i)

print()
print()
print("===============================================================================")
print()
print()

n = 4

for i in range(1, n + 1):

    print((" " * (n - i))+ ("*" * (2 * i - 1)))
for i in range(n-1,0,-1):

    print((" " * (n - i))+ ("*" * (2 * i - 1)))
    

print()
print()
print("===============================================================================")
print()
print()

var=1
n=5
for i in range(0,n):
    for j in range(0,i):
        print(var,end=" ")
        var+=1
    print()

print()
print()
print("===============================================================================")
print()
print()

var=1
n=5
for i in range (0,n):
    print(" "*(n-i),end="")
    for j in range(0,i):
        print(var,end=" ")
        var+=1
    print()
for i in range (n,0,-1):
    print(" "*(n-i),end="")
    for j in range(0,i):
        print(var,end=" ")
        var+=1
    print()















