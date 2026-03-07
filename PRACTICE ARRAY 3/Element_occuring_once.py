#TO FIND THE ELEMENT WHICH OCCURS ONCE 
from numpy import *
a=[1,2,2,3,3,4,5]
n=len(a)
count=0
output=[]
for i in range(0,n):
    count=0
    for j in range(0,n):
       if a[i]==a[j]:
          count+=1
    if count==1:
       output.append(a[i])


print("Unique elements are:")
for i in range(0,len(output)):
   print(output[i])