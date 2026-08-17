class Vectors:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x):
        return f"{self.i + x.i}i + {self.j +x.j}j + {self.k + x.k}k"


v1= Vectors(283,123,342)
v2=Vectors(653,785,247)

print()
print(" ",v1,"\n+",v2)
print("______________________________")
print(v1+v2)