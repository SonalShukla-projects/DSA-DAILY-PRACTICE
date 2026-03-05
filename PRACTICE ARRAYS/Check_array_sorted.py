#TO CHECK WHETHER AN ARRAY IS SORTED OR NOT 
from numpy import *

a=[1,2,33,4,5]
n1=len(a)
flag=1 # array is sorted

for i in range(0,n1-1):
    if a[i] > a[i+1]:
        flag=0
        break

if flag==1:
    print("Array is sorted.")
else:
    print("Array not sorted.")