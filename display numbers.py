n=12345
for i in range(0,5):
    print(" "*i,end="")
    n=n%(10**(5-i))
    print((str(n)).center(5-i," "))


print("------------------------------------")

n=12345
for i in range(0,5):
    v=n//(10**(4-i))
    print(v)