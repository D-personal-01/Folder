
from math import factorial

sum1=0
sum2=0
sum3=0
n=int(input("Enter the number of terms: "))
x=int(input("Enter the value of x: "))
for i in range(1,n+1):
    sum1+=(x**i)*(-1**i)
    for j in range(1,i+1):
        sum2+=j
    
    sum3+=((x**(i-1))/(factorial(i-1))*(-1**(i+1)))

print("The sum of the series are:",sum1+sum2+sum3)