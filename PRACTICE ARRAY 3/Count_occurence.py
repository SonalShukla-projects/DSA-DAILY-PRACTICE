#TO COUNT THE OCCURENCE OF AN ELEMENT IN AN ARRAY
from numpy import *
a=[1,2,2,3,4,5]
n=len(a)
count=0
flag=0 # not found
target=int(input("element to count occurence for:"))
for i in range(0,n):
    if a[i]==target:
        count+=1
        flag=1
if flag==1:
    print("Count of occurence for :",target,"is :",count)
else:
    print("Not found")