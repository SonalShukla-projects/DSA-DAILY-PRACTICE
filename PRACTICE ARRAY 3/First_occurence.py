#TO CHECK FIRST OCCURENCE OF AN ELEMENT
from numpy import *

a=[1,2,2,3,4,5]
n=len(a)
target=int(input("Enter number to find first occurence for:"))
idx=0
flag=0
count=0
for i in range(0,n):
    if a[i]==target:
        count+=1
        idx=i
        flag=1
        
if flag==1:
    print("First occurence at:",idx)
else:
    print("Not present")