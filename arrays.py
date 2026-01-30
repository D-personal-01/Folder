import numpy as np

def array_analysis(arr,n):
    for i in range(0,n):
        print(i,"-->",arr[i])
    print("Array:", arr)
    print("Shape:", arr.shape)
    print("Data Type:", arr.dtype)
    print("Mean:", np.mean(arr))
    print("Standard Deviation:", np.std(arr))
    print("Sum:", np.sum(arr))
    print("Maximum: ",arr.max())
    print("Minimum: ",arr.min())

n = int(input("Enter range: "))

arr=np.arange(n)**2

array_analysis(arr,n)