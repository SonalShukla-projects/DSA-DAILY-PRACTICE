#TO FIND TWO SUM IN AN ARRAY
from numpy import *
a=[2,7,11,15]
n=len(a)
target=int(input("Enter target sum:"))
element=[]
flag=0 # not found
idx=0
idx2=0

for i in range(0,n):
    for j in range(i+1,n):
        if a[i]+a[j]==target:
           element.append(a[i])
           element.append(a[j])
           idx=i
           idx2=j
           flag=1
           break
    

if flag==1:
    print("Elements for twosum are at ",idx,idx2)
    for x in element:
        print(x)
else:
    print("Two sum not present")