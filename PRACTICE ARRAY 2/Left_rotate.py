#TO ROTATE AN ARRAY LEFT

from numpy import *
a=[1,2,3,4,5]
n=len(a)

temp=a[0]

for i in range(0,n-1):
    a[i]=a[i+1]

a[n-1]=temp
print(a)