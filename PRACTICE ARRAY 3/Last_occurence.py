#TO FIND LAST OCCURENCE OF AN ELEMENT
from numpy import *
a=[1,2,2,2,3,4,5]
n=len(a)
target=int(input("Enter element to find last occurence for:"))
idx=0
flag=0
for i in range(0,n):
    if a[i]==target:
        idx=i
        flag=1

if flag==1:
    print("Last occurence at :",idx)
else:
    print("Not present")
