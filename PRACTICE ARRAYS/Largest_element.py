#FIND THE LARGEST ELEMENT IN AN ARRAY

from array import *
arr=array('i',[2,10,1,4,3,71,8,9])
for i in range(0,len(arr)):
    print(arr[i],end=" ")

large=arr[0]
for i in range(1,len(arr)):
    if arr[i]>large:
        large=arr[i]
        
print("\n")
print("Largest element is :",large)