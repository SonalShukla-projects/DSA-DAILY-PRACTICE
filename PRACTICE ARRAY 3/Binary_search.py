#TO FIND THE INDEX OF THE ELEMENT IN AN SORTED ARRAY
from numpy import *
a=[1,2,3,4,5,6]
n=len(a)
target=int(input("Search this element :"))
idx=0
flag=0 # not found

for i in range(0,n-1):
    if a[i]==target:
        flag=1
        idx=i
        break

if flag==1:
    print("Element found at : ",idx,"Element:",target)
else:
    print("Not found.")