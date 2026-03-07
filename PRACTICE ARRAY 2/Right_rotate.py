#TO ROTATE AN ARRAY RIGHT
from numpy import *
a=[1,2,3,4,5]
n=len(a)

temp=a[n-1]

for i in range(n-1,0,-1):
    a[i]=a[i-1]

a[0]=temp
print(a)