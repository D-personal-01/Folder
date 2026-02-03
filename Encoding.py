a=input("Enter the the messege to encode it: ")
list(a)
encoded=""
for j,i in enumerate(a):
    if j%2==0:
        s=ord(i)+17
        encoded=encoded+chr(s)
        continue
    s=(ord(i))**3+25*66
    encoded=encoded+str(s)+"z"
    print(encoded)
