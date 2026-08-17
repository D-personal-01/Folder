class Vectors:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x):
        return Vectors(self.i + x.i, self.j +x.j, self.k + x.k)

    def __mul__(self, x):
        return Vectors(self.i * x.i, self.j * x.j, self.k * x.k)

    def __truediv__(self, x):
        return Vectors(self.i / x.i, self.j /x.j, self.k / x.k)
        


v1= Vectors(283,123,342)
v2=Vectors(653,785,247)

print()
print(" ",v1,"\n+",v2)
print("______________________________")
v3=v1+v2
print(v3)

print()
print(" ",v1,"\n*",v2)
print("______________________________")
v3=v1*v2
print(v3)

print()
print(" ",v1,"\n/",v2)
print("______________________________")
v3=v1/v2
print(v3)