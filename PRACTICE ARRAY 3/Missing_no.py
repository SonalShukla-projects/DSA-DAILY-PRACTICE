# TO FIND THE MISSING NUMBER IN AN ARRAY
from numpy import *
a=[1,3,4,5]
miss=None
n=len(a)

for i in range(0,n):
    if (a[i]+1)!=a[i+1]:
        miss=a[i]+1
        break

print("Missing number is :",miss)

